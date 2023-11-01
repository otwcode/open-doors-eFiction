from unittest import TestCase
from unittest.mock import MagicMock

from efiction import simplified
from opendoors.config import ArchiveConfig

test_logger = MagicMock()
test_sql = MagicMock()
test_config = ArchiveConfig(MagicMock(), "efiction", "efiction/tests/test_data").config


class TestEFictionSimplified(TestCase):
    test_config_no_defs = ArchiveConfig(
        test_logger, "efiction_no_defs", "efiction/tests/test_data"
    ).config
    efiction_with_defs = simplified.EFictionSimplified(
        test_config, test_logger, test_sql
    )
    efiction_no_defs = simplified.EFictionSimplified(
        test_config_no_defs, test_logger, test_sql
    )

    def test_remove_unwanted_tables(self):
        result = self.efiction_no_defs._remove_unwanted_tables(
            [
                "use database;",
                "create table fanfiction_stats;",
                "create table fanfiction_stories;",
            ]
        )
        self.assertTrue(
            "fanfiction_stats" not in result,
            "statements on unwanted tables should be removed",
        )
        self.assertTrue(
            "stories" in result,
            "statements on desired tables should be stripped of their prefix and kept",
        )
