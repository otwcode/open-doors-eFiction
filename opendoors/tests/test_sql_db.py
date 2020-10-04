import glob
import os
import re
from configparser import ConfigParser
from logging import Logger
from unittest import TestCase

from opendoors.config import ArchiveConfig
from opendoors.mysql import SqlDb
from opendoors.utils import get_full_path


class TestSqlDb(TestCase):
    test_logger = Logger("test")
    test_config: ConfigParser = ArchiveConfig(test_logger, "test", "opendoors/tests/test_data").config
    test_sql = SqlDb(test_config, test_logger)

    def tearDown(self) -> None:
        """ Remove any files generated in test_output """
        filtered = [f for f in glob.glob('opendoors/tests/test_output/*') if not re.match(r'\.keep', f)]
        for file in filtered:
            os.remove(file)

    def test_dump_database(self):
        self.test_sql.load_sql_file_into_db(get_full_path("opendoors/tests/test_data/test.sql"))
        self.test_sql.dump_database("od_test_sql", get_full_path("opendoors/tests/test_output/test_output.sql"))
        with open(get_full_path("opendoors/tests/test_output/test_output.sql")) as f:
            result = f.readlines()
            self.assertEqual("(1,'Name1\\'s \\\"stringé\\\"',NULL),\n", result[14])
