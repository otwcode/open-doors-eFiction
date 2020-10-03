"""
Step 04
"""

from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.step_base import StepBase, StepInfo


class Step04(StepBase):
    """
    Step 4.
    """

    def run(self):
        """
        Run step 04
        """
        return self.finish()
