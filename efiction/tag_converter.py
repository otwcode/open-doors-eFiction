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
            original_name = tag_table_name

            if tag_table_name == 'rating':
                tag_table_name = 'ratings'
                id_name = 'rid'
            elif tag_table_name == 'categories':
                id_name = 'catid'
            elif tag_table_name == 'warnings':
                id_name = 'wid'
            elif tag_table_name == 'classes':
                id_name = 'classes'
            elif tag_table_name == 'genres':
                id_name = 'gid'
            elif tag_table_name == 'characters':
                id_name = 'charid'

            query = f"SELECT count(*) as cnt FROM stories WHERE {id_name} NOT IN (SELECT {id_name} FROM {tag_table_name});"

            try:
                count: List[Dict[str, int]] = self.sql.execute_and_fetchall(self.working_original, query)
                tag_tables[original_name] = bool(count and count[0]['cnt'] > 0)
            except Exception as e:
                self.logger.info(e)
                self.logger.info("No such table?")
                tag_tables[original_name] = 0

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
        Convert the eFiction categories table to Open Doors tags.
        :return: Open Doors tags with the original type "categories"
        """
        old_categories, current, total = self.sql.read_table_with_total(self.working_original, "warnings")
        for old_category in old_categories:
            new_tag = {
                'id': old_category['wid'],
                'parent': "",
                'name': old_category['warning'],
                'description': old_category['warning']
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
        Convert the eFiction classes table to Open Doors tags.
        :return: Open Doors tags with the original type "class"
        """
        old_classes, current, total = self.sql.read_table_with_total(self.working_original, "genres")
        for old_class in old_classes:
            new_tag = {
                'id': old_class['gid'],
                'name': old_class['genre'],
                'parent': ""
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
