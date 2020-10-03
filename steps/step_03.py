"""
Step 03
"""

from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.step_base import StepBase, StepInfo


class Step03(StepBase):
    """
    Step 03.
    """

    def run(self):
        """
        Run step 03
        """
        return self.finish()
