from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from opendoors.utils import make_banner, set_working_dir, get_prefixed_path


class UtilsTest(TestCase):
    def test_make_banner_with_padding(self):
        banner1 = make_banner("-", "TEXT", 3)
        self.assertEqual(
            "\n----------\n   TEXT   \n----------",
            banner1,
            "text should be padded by the specified number of spaces",
        )

    def test_make_banner_with_default_padding(self):
        banner2 = make_banner("-", "TEXT")
        self.assertEqual(
            "\n--------\n  TEXT  \n--------",
            banner2,
            "text should be padded by two spaces when no padding is specified",
        )

    @patch("opendoors.utils.os.makedirs")
    def test_set_working_dir_with_path(self, mock_makedirs):
        working_dir1 = set_working_dir("new_path", "archive_code")
        mock_makedirs.assert_called_with("new_path")
        self.assertEqual(
            "new_path", working_dir1, "`path` parameter should be used if supplied"
        )

    @patch("builtins.input", lambda *args: "")
    def test_set_working_dir_without_path(self):
        working_dir_2 = set_working_dir(None, "archive_code")
        self.assertEqual(
            str(Path().home() / "otw_opendoors" / "archive_code"),
            working_dir_2,
            "a path based on the user folder should be used if no path is supplied",
        )

    def test_prefixed_path_no_filename(self):
        base_path = str(Path().home() / "otw_opendoors")
        test_path = get_prefixed_path("01", base_path)
        full_path = str(Path().home() / "otw_opendoors" / "efiction-01")
        self.assertEqual(
            full_path, test_path, "step folder should be created in lieu of filename"
        )

    def test_prefixed_path_with_filename(self):
        prefix = "efiction-01"
        base_path = str(Path().home() / "otw_opendoors" / prefix)
        file_name = "test_working_open_doors.sql"
        test_path = get_prefixed_path("01", base_path, file_name)
        full_path = str(
            Path().home() / "otw_opendoors" / prefix / f"{prefix}-{file_name}"
        )
        self.assertEqual(full_path, test_path, "filename should be prefixed with step")
