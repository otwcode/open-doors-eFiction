from logging import Logger
from unittest import TestCase
from unittest.mock import patch

from opendoors.config import ArchiveConfig


class ConfigTest(TestCase):
    @patch('builtins.input', lambda *args: 'test')
    @patch('builtins.open')
    @patch('opendoors.config.configparser.ConfigParser.write')
    def test_save(self, mock_write, mock_open):
        config = ArchiveConfig(Logger("test"), "test", "working_dir")
        self.assertEqual("test", config.config["Archive"]["code_name"])
