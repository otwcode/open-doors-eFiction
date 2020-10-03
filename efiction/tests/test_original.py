from unittest import TestCase
from unittest.mock import MagicMock, patch

from efiction.original import EFictionOriginal
from opendoors.config import ArchiveConfig

test_logger = MagicMock()
test_sql = MagicMock()
test_config = ArchiveConfig(MagicMock(), "efiction", "efiction/tests/test_data").config


class TestOriginal(TestCase):

    @patch('builtins.input', lambda *args: 'efiction/tests/test_data/efiction.sql')
    @patch('efiction.original.add_create_database')
    def test_load_original_file(self, mock_add_create_database):
        efiction = EFictionOriginal(test_config, test_logger, test_sql)
        efiction.load_original_file("path")
        mock_add_create_database.assert_called_once()
        test_sql.load_sql_file_into_db.assert_called_once_with("path/efictiontest_efiction_original_edited.sql")
