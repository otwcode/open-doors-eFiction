"""
Step 01
"""
import os
from configparser import ConfigParser
from logging import Logger

from efiction.eFiction_table_defs import create_def
from opendoors.mysql import SqlDb
from opendoors.sql_utils import write_statements_to_file, parse_remove_comments, group_by_table, add_create_database
from opendoors.utils import copy_to_dir, check_if_file_exists, get_full_path


class EFictionOriginal:
    """
    Copies the original eFiction database dump to the working directory, adds table definitions if they are missing,
    and loads the result into MySQL for future reference
    """

    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb):
        self.sql = sql
        self.config = config
        self.logger = logger
        self.code_name = config['Archive']['code_name']
        self.original_db_name = f"{self.code_name}_efiction_original"
        self.edited_file_name = f"{self.code_name}_efiction_original_edited.sql"

    @staticmethod
    def _contains_table_defs(grouped_statements):
        """
        Does the provided list of statements contain create table statements?
        :return: True or False
        """
        statements = [item for sublist in grouped_statements.values() for item in sublist]
        return any(str.lower(elem).startswith("create table") for elem in statements)

    def __backup_original(self):
        """
        Check if the backup file is already configured and exists, or copy the original db dump to the backup file
        :return: the path to the backup file
        """
        # Prompt for original db file if we don't already have it in the config
        if not (self.config.has_option('Archive', 'original_db_file_path')) or \
                self.config['Archive']['original_db_file_path'] == "":
            path_to_original_db = input("Full path to the original database file "
                                        "(this will be copied into the working path and loaded into MySQL):\n>> ")
            self.config['Archive']['original_db_file_path'] = path_to_original_db

        # Return the existing file or create a backup of the original db dump
        if check_if_file_exists(self.config, 'Processing', 'backup_file'):
            backup_file = self.config['Processing']['backup_file']
            self.logger.info("Using backup file {}".format(backup_file))
        else:
            backup_file = copy_to_dir(old_file_path=self.config['Archive']['original_db_file_path'],
                                      new_file_dir=self.config['Processing']['working_dir'],
                                      new_file_name=f"{self.code_name}_original_db_backup.sql")
            self.config['Processing']['backup_file'] = backup_file
            self.logger.info(f"Created backup of original file at {backup_file}")
        return backup_file

    def _add_table_definitions(self, statements: list):
        """
        SQL backups performed from within eFiction don't contain table definitions. Add drop and create table
        statements if this is the case.
        :param statements: original SQL statements
        :return: dict of SQL statements grouped by table names
        """
        grouped_statements = group_by_table(statements)
        if not self._contains_table_defs(grouped_statements):
            new_grouped_statements = {}
            for (table_name, statements) in grouped_statements.items():
                new_grouped_statements[table_name] = create_def(table_name) + statements
            groups = new_grouped_statements
        else:
            groups = grouped_statements
        return [item for sublist in list(groups.values()) for item in sublist]

    def __add_definitions(self):
        """
        Remove comments and if needed, add table definitions to the original eFiction database
        :param step_path: the destination path for the file backup
        """
        self.logger.info("\nAdding table definitions and removing comments from original eFiction database")

        self.logger.info("...adding table definitions and tidying original db dump...")
        with open(get_full_path(self.config['Processing']['backup_file']), "r") as f:
            original_db_sql = f.read()
        clean_statements = parse_remove_comments(original_db_sql)
        statements_with_defs = self._add_table_definitions(clean_statements)
        return add_create_database(self.original_db_name, statements_with_defs)

    def __load_into_database(self, step_path, statements):
        """

        :param step_path: the destination path for the edited file
        :param statements: the edited SQL statements
        :return:
        """
        self.logger.info("...writing edited SQL statements to a backup file...")
        edited_file_path = os.path.join(step_path, self.edited_file_name)
        self.config['Processing']['original_edited_file'] = edited_file_path
        edited_file = write_statements_to_file(self.config['Processing']['original_edited_file'], statements)

        self.logger.info("...loading edited original database into MySQL...")
        self.sql.load_sql_file_into_db(edited_file)

    def load_original_file(self, step_path):
        """
        Take the original eFiction backup, add table definitions if needed, and load into MySQL for reference
        :param step_path: full path to the folder for this step
        """
        self.logger.info("Processing original eFiction database...")
        self.__backup_original()
        statements = self.__add_definitions()
        self.__load_into_database(step_path, statements)
