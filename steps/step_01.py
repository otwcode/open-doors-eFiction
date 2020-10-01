"""
Step 01
"""

from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.step_base import StepBase, StepInfo


class Step01(StepBase):
    """
    Step 01
    """

    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb, step_info: StepInfo):
        super().__init__(config, logger, sql, step_info)

    def run(self):
        """
        Run step 01
        """
        return self.finish()
