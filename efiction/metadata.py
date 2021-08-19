import os
import re
from configparser import ConfigParser
from logging import Logger

from unidecode import unidecode

from efiction.tag_converter import TagConverter
from opendoors.mysql import SqlDb
from opendoors.sql_utils import parse_remove_comments, write_statements_to_file, add_create_database
from opendoors.utils import print_progress, get_full_path, normalize, key_find
from opendoors.thread_pool import ThreadedPool
from opendoors.big_insert import BigInsert


class EFictionMetadata:
    """
    Create and populate Open Doors tables and extract tags to a separate table for later export to Tag Wrangling.
    """

    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb, step_path: str):
        self.config = config
        self.sql = sql
        self.logger = logger
        self.working_original = self.config['Processing']['simplified_original_db'] if self.config.has_option(
            'Processing', 'simplified_original_db') else None
        self.create_open_doors_db(step_path)
        self.working_open_doors = self.config['Processing']['open_doors_working_db']
        self.tag_converter = TagConverter(config, logger, sql)
        self.authors = []
        self.ratings = []
        self.ratings_nonstandard: bool = False
        self.categories = []
        self.classes = []
        self.characters = []

    def create_open_doors_db(self, step_path):
        """
        Create a blank working Open Doors database
        :param step_path: Path for the current step, where the database backup will be saved.
        :return: True if successful
        """
        od_table_sql_file = get_full_path('opendoors/open-doors-tables-working.sql')
        self.config['Processing']['open_doors_working_db'] = \
            f"{self.config['Archive']['code_name']}_working_open_doors"
        self.config['Processing']['open_doors_working_db_file'] = \
            os.path.join(step_path, f"{self.config['Processing']['open_doors_working_db']}.sql")

        with open(od_table_sql_file, "r") as f:
            od_table_defs = parse_remove_comments(f.read())
        statements = add_create_database(self.config['Processing']['open_doors_working_db'], od_table_defs)
        od_tables = write_statements_to_file(self.config['Processing']['open_doors_working_db_file'], statements)
        self.sql.load_sql_file_into_db(od_tables)
        return True

    @staticmethod
    def generate_email(name: str, email: str, archive_long_name: str):
        """
        If no email address is provided, generate an ASCII email address at ao3.org by transliterating the username and
        archive long title
        :param name: the author's original display name
        :param email: the author's current email address
        :param archive_long_name: the long name of the archive being processed
        :return: An ASCII ao3.org email address
        """
        if email:
            return email.strip()
        else:
            user = name.title() + archive_long_name.title()
            return re.sub(r'\W+', '', unidecode(user)) + 'Archive@ao3.org'

    def _convert_authors(self, old_authors=None):
        self.logger.info("Converting authors...")
        current = 0
        total = len(old_authors)
        insert_op = BigInsert(
                self.working_open_doors,
                "authors",
                ["id", "name", "email"],
                self.sql
            )
        for old_author in old_authors:
            new_author = {
                'id': old_author['uid'],
                'name': old_author['penname'],
                'email': self.generate_email(old_author['penname'], old_author['email'],
                                             self.config['Archive']['archive_name'])
            }
            insert_op.addRow(new_author['id'], new_author["name"], new_author["email"])
            current = print_progress(current, total, "authors converted")
        insert_op.send()
        return self.sql.read_table_to_dict(self.working_open_doors, "authors")

    def _convert_characters(self, old_characters):
        current, total = (0, len(old_characters))
        insert_op = BigInsert(
            self.working_open_doors,
            "tags",
            ["original_tagid", "original_tag", "original_type", "original_parent"],
            self.sql
        )
        for old_character in old_characters:
            parent = [ct['original_tag'] for ct in self.categories if ct['original_tagid'] == old_character['catid']]
            new_tag = {
                'id': old_character['charid'],
                'name': old_character['charname'],
                'parent': ", ".join(parent) if parent != [] else ""
            }
            insert_op.addRow(new_tag["id"], new_tag["name"], "character", new_tag["parent"])
            current = print_progress(current, total, "characters converted")
        insert_op.send()
        return self.sql.execute_and_fetchall(self.working_open_doors,
                                             "SELECT * FROM tags WHERE `original_type` = 'character'")

    def _convert_story_tags(self, old_story):
        old_tags = {
            'rating': key_find('rid', old_story, '').split(','),
            'categories': key_find('catid', old_story, '').split(','),
            'classes': key_find('classes', old_story, '').split(','),
            'characters': key_find('charid', old_story, '').split(',')
        }

        if self.ratings_nonstandard:
            ratings = [r['id'] for r in self.ratings if str(r['original_tag']) in old_tags['rating']]
        else:
            ratings = [r['id'] for r in self.ratings if str(r['original_tagid']) in old_tags['rating']]
        categories = [c['id'] for c in self.categories if str(c['original_tagid']) in old_tags['categories']]
        classes = [c['id'] for c in self.classes if str(c['original_tagid']) in old_tags['classes']]
        characters = [c['id'] for c in self.classes if str(c['original_tagid']) in old_tags['characters']]

        return {
            'rating': ratings,
            'categories': categories,
            'classes': classes,
            'characters': characters
        }

    def _convert_tags_join(self, new_story, tags, sql=None):
        full_query = f"INSERT INTO item_tags (item_id, item_type, tag_id) VALUES "
        tag_query = []
        for tag_list in tags.values():
            for tag in tag_list:
                tag_query.append(f"""{new_story['id'], "story", tag}""")
        full_query += ", ".join(tag_query)
        if sql is None:
            self.sql.execute(self.working_open_doors, full_query)
        else:
            sql.execute(self.working_open_doors, full_query)

    def _convert_author_join(self, new_story, author_id, sql=None):
        full_query = f"""INSERT INTO item_authors (item_id, item_type, author_id) VALUES 
                     {new_story['id'], "story", author_id}"""
        if sql is None:
            self.sql.execute(self.working_open_doors, full_query)
        else:
            sql.execute(self.working_open_doors, full_query)

    def fetch_coauthors(self, new_story, sql=None):
        coauthors = []
        # access the coauthors table using the story ID
        full_query = f"""SELECT * FROM coauthors WHERE sid = {new_story['id']};"""
        # get a dict of coauthor IDs for the story
        if sql is None:
            authors = self.sql.execute_and_fetchall(self.working_original, full_query)
        else:
            authors = sql.execute_and_fetchall(self.working_original, full_query)
        # We only try to operate on this result if it is not None
        if authors:
            for author in authors:
                coauthors.append(author['uid'])
        return coauthors

    def convert_stories(self, language_code):
        """
        Convert eFiction stories to the Open Doors format. Note that we leave all the tag columns (rating, relationships,
        tags, categories etc) empty because they are all in the `tags` table and will be populated with AO3 tags when
        this archive is processed in the ODAP.
        :return: The Open Doors stories table as a dict.
        """
        self.logger.info("Converting stories...")
        old_stories, current, total = self.sql.read_table_with_total(self.working_original, "stories")
        def story_processor(old_story):
            """
            Lambda-esque function that clones connection to database and 
            fully converts the given story
            :param old_story: Original story read from the database
            """
            sql = self.sql.get_another_connection()
            new_story = {
                'id': old_story['sid'],
                'title': key_find('title', old_story, '').strip(),
                'summary': normalize(old_story['summary']),
                'notes': key_find('storynotes', old_story, '').strip(),
                'date': str(old_story['date']),
                'updated': str(old_story['updated']),
                'language_code': language_code
            }

            self.logger.debug(f"Converting story metadata for '{new_story['title']}'")
            query = f"""
            INSERT INTO stories (id, title, summary, notes, date, updated, language_code)
            VALUES {new_story['id'], new_story['title'], new_story['summary'],
                    new_story['notes'], new_story['date'], new_story['updated'], new_story['language_code']};
            """
            sql.execute(self.working_open_doors, query)

            self.logger.debug(f"  tags...")
            tags = self._convert_story_tags(old_story)
            # pass the new sql to be used instead of the main one
            self._convert_tags_join(new_story, tags, sql)

            self.logger.debug(f"  authors...")
            self._convert_author_join(new_story, old_story['uid'], sql)
            # Find if there are any coauthors for the work
            coauthors = self.fetch_coauthors(new_story, sql)
            for coauthor in coauthors:
                self._convert_author_join(new_story, coauthor, sql)
        
        # if you give to little threads, it will be too slow,
        # if you give too much - it will fail while attempting to connect to db
        # (mysql does not like 200 connections); 20 seems to be a nice balance
        pool = ThreadedPool(20)
        pool.map(story_processor, [[x] for x in old_stories])

        return self.sql.execute_and_fetchall(self.working_open_doors, "SELECT * FROM stories")

    def convert_all_tags(self):
        """
        Extract all tags by category.
        """
        self.ratings = self.tag_converter.convert_ratings()
        self.ratings_nonstandard = self.tag_converter.check_for_nonstandard_ratings()
        self.categories = self.tag_converter.convert_categories()
        self.classes = self.tag_converter.convert_classes()

        old_characters = self.sql.read_table_to_dict(self.working_original, "characters")
        self.characters = self._convert_characters(old_characters)

    def convert_original_to_open_doors(self, step_path: str):
        """
        Convert eFiction tables to Open Doors tables
        :return: True if the process was successful
        """
        self.logger.info("Converting metadata tables from eFiction to Open Doors structure...")

        self.convert_all_tags()

        old_authors = self.sql.read_table_to_dict(self.working_original, "authors")
        self.authors = self._convert_authors(old_authors)

        # Prompt for original db file if we don't already have it in the config
        if not self.config.has_option('Archive', 'language_code'):
            language = input("Two-letter Language code of the stories in this archive (default: en - press enter):\n>> ")
            self.config['Archive']['language_code'] = language
        else:
            language = self.config['Archive']['language_code']

        self.convert_stories(language)

        database_dump = os.path.join(step_path, f"{self.working_open_doors}_without_chapters.sql")
        self.logger.info(f"Exporting converted tables to {database_dump}...")
        self.sql.dump_database(self.working_open_doors, database_dump)
        return True
