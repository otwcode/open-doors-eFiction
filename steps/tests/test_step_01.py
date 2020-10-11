import glob
import os
import re
import shutil
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch

from opendoors.config import ArchiveConfig
from opendoors.step_base import StepInfo
from steps.step_01 import Step01

test_logger = MagicMock()
test_sql = MagicMock()
test_config = ArchiveConfig(MagicMock(), "test", "steps/tests/test_data").config


class TestStep01(TestCase):
    def tearDown(self) -> None:
        """ Remove any files generated in test_output """
        filtered = [f for f in glob.glob('steps/tests/test_output/*') if not re.match(r'\.keep', f)]
        for file in filtered:
            try:
                if Path(file).is_dir():
                    shutil.rmtree(file)
                else:
                    os.remove(file)
            except PermissionError as pe:
                # We don't necessarily care that much
                continue

    @patch('builtins.input', lambda *args: 'efiction/tests/test_data/efiction.sql')
    def test_run(self):
        step_info = StepInfo("test_output/01", "Test step 01", "02")
        thing = Step01(test_config, test_logger, test_sql, step_info).run()
        self.assertEqual(thing, True)
