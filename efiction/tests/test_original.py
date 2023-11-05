from unittest import TestCase
from unittest.mock import MagicMock, patch

from efiction.original import EFictionOriginal
from opendoors.config import ArchiveConfig
from opendoors.sql_utils import group_by_table
from opendoors.utils import remove_output_files

test_logger = MagicMock()
test_sql = MagicMock()
test_config = ArchiveConfig(MagicMock(), "efiction_no_defs", "efiction/tests/test_data").config


class TestOriginal(TestCase):
    test_config_no_defs = ArchiveConfig(test_logger, "efiction_no_defs", "efiction/tests/test_data").config
    efiction_with_defs = EFictionOriginal(test_config, test_logger, test_sql)
    efiction_no_defs = EFictionOriginal(test_config_no_defs, test_logger, test_sql)

    def tearDown(self) -> None:
        """ Remove files created during the tests """
        remove_output_files('efiction/tests/test_output/*')

    @patch('builtins.input', lambda *args: 'efiction/tests/test_data/efiction.sql')
    @patch('efiction.original.add_create_database')
    def test_load_original_file(self, mock_add_create_database):
        self.efiction_with_defs.load_original_file("efiction/tests/test_output")
        mock_add_create_database.assert_called_once()
        test_sql.load_sql_file_into_db.arg_should_contain("efictiontestnodefs_efiction_original_edited.sql")

    def test_check_for_table_defs_no_defs(self):
        statements = group_by_table(
            ['INSERT INTO fanfiction_authorinfo VALUES ("0","2","http://example.com")',
             'INSERT INTO fanfiction_authorprefs VALUES	("5","BillBob","2","0","1","77")',
             'INSERT INTO fanfiction_authors VALUES	("1","Author1","Author1","A1@example.com")']
        )
        has_defs = EFictionOriginal._contains_table_defs(statements)
        self.assertFalse(has_defs)

    def test_check_for_table_defs_with_defs(self):
        statements = group_by_table(
            ['CREATE TABLE fanfiction_authorinfo (`uid` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(200))',
             'INSERT INTO fanfiction_authorinfo VALUES	("5","BillBob","2","0","1","77")',
             'INSERT INTO fanfiction_authors VALUES	("1","Author1","Author1","A1@example.com")']
        )
        has_defs = self.efiction_with_defs._contains_table_defs(statements)
        self.assertTrue(has_defs)

    def test_add_table_definitions(self):
        statements = ['INSERT INTO fanfiction_authorinfo VALUES ("0","2","http://example.com")',
                      "INSERT INTO fanfiction_stories VALUES ('1', 'thing');"]
        result = self.efiction_no_defs._add_table_definitions(statements)
        self.assertEqual("DROP TABLE IF EXISTS `fanfiction_stories`;", result[3].strip(),
                         "should generate DROP TABLE statements for the given tables")
        self.assertTrue(result[4].strip().startswith("CREATE TABLE `fanfiction_stories`"),
                        "should generate CREATE TABLE statements for the given tables")
