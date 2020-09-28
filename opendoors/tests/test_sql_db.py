from logging import Logger
from unittest import TestCase

from configparser import ConfigParser

from opendoors.config import ArchiveConfig
from opendoors.mysql import SqlDb
from opendoors.utils import get_full_path

test_logger = Logger("test")
test_config: ConfigParser = ArchiveConfig(test_logger, "efiction", "opendoors/tests/test_data").config
test_sql = SqlDb(test_config, test_logger)


class TestSqlDb(TestCase):

    def test_dump_database(self):
        test_sql.load_sql_file_into_db(get_full_path("opendoors/tests/test.sql"))
        test_sql.dump_database("od_test_sql", get_full_path("opendoors/tests/test_output/test_output.sql"))
        with open(get_full_path("opendoors/tests/test_output/test_output.sql")) as f:
            result = f.readlines()
            self.assertEqual("(1,'Name1\\'s \\\"stringé\\\"',NULL),\n", result[14])
