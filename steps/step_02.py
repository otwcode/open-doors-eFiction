"""
Step 02
"""

from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.step_base import StepBase, StepInfo


class Step02(StepBase):
    """
    Step 02.
    """

    def run(self):
        """
        Run step 02
        """
        return self.finish()
