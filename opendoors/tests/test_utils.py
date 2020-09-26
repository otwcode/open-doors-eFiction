from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from opendoors.utils import make_banner, set_working_dir


class UtilsTest(TestCase):
    def test_make_banner_with_padding(self):
        banner1 = make_banner('-', "TEXT", 3)
        self.assertEqual("\n----------\n   TEXT   \n----------", banner1)

    def test_make_banner_with_default_padding(self):
        banner2 = make_banner('-', "TEXT")
        self.assertEqual("\n--------\n  TEXT  \n--------", banner2)

    @patch('opendoors.utils.os.makedirs')
    def test_set_working_dir_with_path(self, mock_makedirs):
        working_dir1 = set_working_dir("new_path", "archive_code")
        mock_makedirs.assert_called_with("new_path")
        self.assertEqual("new_path",
                         working_dir1,
                         "`path` parameter should be used if supplied")

    @patch('builtins.input', lambda *args: '')
    def test_set_working_dir_without_path(self):
        working_dir_2 = set_working_dir(None, "archive_code")
        self.assertEqual(str(Path().home() / "otw_opendoors" / "archive_code"),
                         working_dir_2,
                         "a path based on the user folder should be used if no path is supplied")
