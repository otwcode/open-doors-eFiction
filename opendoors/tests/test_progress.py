from logging import Logger

from configparser import ConfigParser
from unittest import TestCase
from unittest.mock import patch, MagicMock

from opendoors.config import ArchiveConfig
from opendoors.progress import continue_from_last
from opendoors.step_base import StepBase, StepInfo

test_logger = MagicMock()
test_config: ConfigParser = ArchiveConfig(test_logger, "efiction", "opendoors/tests/test_data").config
test_sql = MagicMock()


class Step1(StepBase):
    """Test Step 1"""

    def run(self):
        """Run Test Step 1"""
        return True


class Step2(StepBase):
    """Test Step 2"""

    def run(self):
        """Run Test Step 2"""
        return True


steps = {
    '01': {'info': StepInfo(next_step='02', step_description='Step 1', step_number='01'), 'class': Step1},
    '02': {'info': StepInfo(next_step='None', step_description='Step 2', step_number='02'), 'class': Step2}
}


class TestProgress(TestCase):
    @patch('builtins.input', lambda *args: '2')
    def test_continue_from_last(self):
        thing = continue_from_last(test_config, test_logger, test_sql, steps)
        self.assertIsNone(thing)
        self.assertSetEqual(set("01, 02".split(', ')), set(test_config['Processing']['done_steps'].split(', ')))
