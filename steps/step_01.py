"""
Step 01
"""

from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.step_base import StepBase, StepInfo


class Step01(StepBase):
    """
    Load original database file into MySQL for future reference
    """

    def run(self):
        """
        Run step 01
        """
        self.logger.info("Step 01 in progress")
        return self.finish()
