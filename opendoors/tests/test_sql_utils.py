from unittest import TestCase

from opendoors import sql_utils


class TestSqlUtils(TestCase):
    statements = [
        """drop table if exists `thingy_stories`;""",
        """DROP TABLE IF EXISTS `fanfictionstories`;""",
        """CREATE TABLE fanfiction_stories (
          `sid` int(11) NOT NULL AUTO_INCREMENT,
          `title` varchar(200) NOT NULL DEFAULT '',
          PRIMARY KEY (`sid`),
          KEY `title` (`title`)
        ) ENGINE=MyISAM AUTO_INCREMENT=311 DEFAULT CHARSET=latin1;""",
        """insert into thingy_stories VALUES ("1", "thing");""",
        """insert into thingy_stories VALUES ("2", "thing");""",
        """insert into thingy_polls VALUES ("3", "thing");"""
    ]

    def test_extract_table_name_lower_with_underscore_and_backtick(self):
        result = sql_utils.extract_table_name(self.statements[0])
        self.assertEqual(result, 'thingy_stories')

    def test_extract_table_name_upper_no_underscore_with_backtick(self):
        result = sql_utils.extract_table_name(self.statements[1])
        self.assertEqual(result, 'fanfictionstories')

    def test_extract_table_name_upper_with_underscore_no_backtick(self):
        result = sql_utils.extract_table_name(self.statements[2])
        self.assertEqual(result, 'fanfiction_stories')

    def test_group_by_table(self):
        result = sql_utils.group_by_table(self.statements)
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result['fanfiction_stories'], list)
        self.assertEqual(3, len(result['thingy_stories']))
