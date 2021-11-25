import os
import re
from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.sql_utils import group_by_table, add_create_database, parse_remove_comments, write_statements_to_file
from opendoors.utils import get_full_path, get_prefixed_path


class EFictionSimplified:
    """
    Removes tables that are not needed for Open Doors imports
    """

    # EFiction names its tables as xxxxx_tablename and we only need to keep a few to process the archive
    tables_to_keep = (
        "authors", "categories", "challenges", "chapters", "characters", "classes", "classtypes", "coauthors",
        "inseries", "ratings", "series", "stories", "warnings", "genres")

    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb):
        self.sql = sql
        self.config = config
        self.logger = logger
        self.code_name = config['Archive']['code_name']
        self.simplified_db_name = f"{self.code_name}_efiction_original_simplified"
        self.simplified_file_name = f"{self.code_name}_efiction_original_simplified.sql"

    def __is_table_to_keep(self, table_name: str):
        """
        Check if the suffix of the table name is in the tables to keep list
        :param table_name: str. Name of the table to check
        :return: True or False
        """
        return str.lower(table_name).endswith(self.tables_to_keep)

    @staticmethod
    def __strip_prefix(table_name: str, statements: list):
        new_name = re.sub(r'\S+_', '', table_name)
        new_statements = [item.replace(table_name, new_name) for item in statements]
        return new_name, new_statements

    def _remove_unwanted_tables(self, statements):
        """
        Strip out any statements affecting tables we don't need (like stats and author favourites)
        :return: the tables to keep
        """
        groups = group_by_table(statements)
        grouped_statements = {}
        for k, v in groups.items():
            if self.__is_table_to_keep(k):
                key, value = self.__strip_prefix(k, v)
                grouped_statements[key] = value
            elif k in ["", "lock", "unlock", "alter", "commit", "drop", "create", "use", "set", "start"]:
                # Ignore some side-effects of the table extraction
                pass
            else:
                self.logger.info("Discarding table: {}".format(k))
        return grouped_statements

    def __simplify_and_load_statements(self, statements, step_path):
        """
        Remove unwanted tables from the efiction database
        :param statements: original efiction tables with definitions
        :param step_path: destination path for the file backup
        :return:
        """
        self.logger.info("Stripping unwanted information from eFiction tables...")
        grouped_statements = self._remove_unwanted_tables(statements)

        # Flatten grouped SQL statements and add CREATE DATABASE statement
        output_filename = get_prefixed_path("02", step_path, f"{self.simplified_db_name}.sql")
        flattened_statements = [item for sublist in list(grouped_statements.values()) for item in sublist]
        final_statements = add_create_database(self.simplified_db_name, flattened_statements)

        self.logger.info("...writing simplified original tables to file...")
        self.config['Processing']['simplified_original_db'] = self.simplified_db_name
        step01_working_db = write_statements_to_file(output_filename, final_statements)

        self.logger.info("...removing any existing simplified original database in MySQL...")
        self.sql.drop_database(self.simplified_db_name)

        self.logger.info("...loading simplified original tables into MySQL...")
        self.sql.load_sql_file_into_db(step01_working_db)

    def simplify_original_file(self, step_path) -> bool:
        """
        Take the original eFiction backup, remove unwanted tables and save the result as the "working" database
        :param step_path: full path to the folder for this step
        :return: True if nothing went wrong
        """
        self.logger.info("\nProcessing edited original eFiction database...")
        with open(get_full_path(self.config['Processing']['original_edited_file']), "r", encoding="utf-8") as f:
            statements = f.read()
        self.__simplify_and_load_statements(parse_remove_comments(statements), step_path)

        return True
