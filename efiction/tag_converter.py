from configparser import ConfigParser
from logging import Logger

from typing import Dict, List

from opendoors.mysql import SqlDb
from opendoors.utils import print_progress


class TagConverter:
    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb):
        self.logger = logger
        self.config = config
        self.sql = sql
        self.working_original = self.config['Processing']['simplified_original_db']
        self.working_open_doors = self.config['Processing']['open_doors_working_db']

    def check_for_nonstandard_tag_tables(self) -> bool:
        """
        Determine whether or not the given eFiction tag table correctly uses IDs,
        or if it is 'non-standard' from using tag names as identifiers
        :return: True if non-standard, otherwise False
        """

        tag_tables = {}

        for tag_table_name in ['rating', 'categories', 'warnings', 'classes', 'genres', 'characters']:

            if tag_table_name == 'rating':
                # Only one rating per story, so story rating should be single number
                # that exactly matches rating id
                query = "SELECT count(*) as cnt FROM stories WHERE rid NOT IN (SELECT rid FROM ratings);"
                count: List[Dict[str, int]] = self.sql.execute_and_fetchall(self.working_original, query)
                tag_tables['rating'] = bool(count and count[0]['cnt'] > 0)
            else:
                # Rough check: ensure all identifiers for tag table are integers

                if tag_table_name == 'categories':
                    id_name = 'catid'
                elif tag_table_name == 'warnings':
                    id_name = 'wid'
                elif tag_table_name == 'classes':
                    id_name = 'classes'
                elif tag_table_name == 'genres':
                    id_name = 'gid'
                elif tag_table_name == 'characters':
                    id_name = 'charid'

                try:
                    query = f"SELECT {id_name} FROM stories;"
                    tags = self.sql.execute_and_fetchall(self.working_original, query)
                    try:
                        tags = list(map(lambda story_tags: story_tags[id_name].replace(',', ''), tags))
                        int(''.join(tags))
                        tag_tables[tag_table_name] = False
                    except Exception:
                        # Non-integer in identifier
                        tag_tables[tag_table_name] = True
                except Exception as e:
                    self.logger.info(e)
                    self.logger.info("No such table?")
                    tag_tables[tag_table_name] = None

        return tag_tables


    def convert_ratings(self):
        """
        Convert the eFiction ratings table to Open Doors tags.
        :return: Open Doors tags with the original type "rating"
        """
        old_ratings, current, total = self.sql.read_table_with_total(self.working_original, "ratings")
        for old_rating in old_ratings:
            new_rating = {
                'id': old_rating['rid'],
                'name': old_rating['rating'],
                'description': old_rating['warningtext']
            }
            query = f"""
                INSERT INTO tags (`original_tagid`, `original_tag`, `original_type`, `original_description`)
                VALUES {new_rating['id'], new_rating['name'], 'rating', new_rating['description']};
                """
            self.sql.execute(self.working_open_doors, query)
            current = print_progress(current, total, "ratings converted")
        return self.sql.execute_and_fetchall(self.working_open_doors,
                                             "SELECT * FROM tags WHERE `original_type` = 'rating';")

    def convert_categories(self):
        """
        Convert the eFiction categories table to Open Doors tags.
        :return: Open Doors tags with the original type "categories"
        """
        old_categories, current, total = self.sql.read_table_with_total(self.working_original, "categories")
        for old_category in old_categories:
            parent = [cat['category'] for cat in old_categories if cat['catid'] == old_category['parentcatid']]
            new_tag = {
                'id': old_category['catid'],
                'parent': ", ".join(parent) if parent != [] else "",
                'name': old_category['category'],
                'description': old_category['description']
            }
            query = f"""
            INSERT INTO tags 
                (`original_tagid`, `original_tag`, `original_type`, `original_description`, `original_parent`)
            VALUES {new_tag['id'], new_tag['name'], 'category', new_tag['description'], new_tag['parent']};
            """
            self.sql.execute(self.working_open_doors, query)
            current = print_progress(current, total, "categories converted")
        return self.sql.execute_and_fetchall(self.working_open_doors,
                                             "SELECT * FROM tags WHERE `original_type` = 'category'")

    def convert_warnings(self):
        """
        Convert the eFiction warnings table to Open Doors tags.
        :return: Open Doors tags with the original type "warnings"
        """
        old_warnings, current, total = self.sql.read_table_with_total(self.working_original, "warnings")
        for old_warning in old_warnings:
            new_tag = {
                'id': old_warning['wid'],
                'parent': "",
                'name': old_warning['warning'],
                'description': old_warning['warning']
            }
            query = f"""
            INSERT INTO tags 
                (`original_tagid`, `original_tag`, `original_type`, `original_description`, `original_parent`)
            VALUES {new_tag['id'], new_tag['name'], 'warning', new_tag['description'], new_tag['parent']};
            """
            self.sql.execute(self.working_open_doors, query)
            current = print_progress(current, total, "warnings converted")
        return self.sql.execute_and_fetchall(self.working_open_doors,
                                             "SELECT * FROM tags WHERE `original_type` = 'warning'")

    def convert_classes(self):
        """
        Convert the eFiction classes table to Open Doors tags.
        :return: Open Doors tags with the original type "class"
        """
        old_classes, current, total = self.sql.read_table_with_total(self.working_original, "classes")
        old_class_types, _, _ = self.sql.read_table_with_total(self.working_original, "classtypes")
        for old_class in old_classes:
            parent = [ct['classtype_title'] for ct in old_class_types if ct['classtype_id'] == old_class['class_type']]
            new_tag = {
                'id': old_class['class_id'],
                'name': old_class['class_name'],
                'parent': ", ".join(parent) if parent != [] else ""
            }
            query = f"""
            INSERT INTO tags 
                (`original_tagid`, `original_tag`, `original_type`, `original_parent`)
            VALUES {new_tag['id'], new_tag['name'], 'class', new_tag['parent']};
            """
            self.sql.execute(self.working_open_doors, query)
            current = print_progress(current, total, "classes converted")
        return self.sql.execute_and_fetchall(self.working_open_doors,
                                             "SELECT * FROM tags WHERE `original_type` = 'class'")

    def convert_genres(self):
        """
        Convert the eFiction genres table to Open Doors tags.
        :return: Open Doors tags with the original type "genre"
        """
        old_genres, current, total = self.sql.read_table_with_total(self.working_original, "genres")
        for old_genre in old_genres:
            new_tag = {
                'id': old_genre['gid'],
                'name': old_genre['genre'],
                'parent': ""
            }
            query = f"""
            INSERT INTO tags 
                (`original_tagid`, `original_tag`, `original_type`, `original_parent`)
            VALUES {new_tag['id'], new_tag['name'], 'genre', new_tag['parent']};
            """
            self.sql.execute(self.working_open_doors, query)
            current = print_progress(current, total, "genres converted")
        return self.sql.execute_and_fetchall(self.working_open_doors,
                                             "SELECT * FROM tags WHERE `original_type` = 'genre'")
