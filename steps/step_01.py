"""
Step 01
"""

from opendoors.step_base import StepBase


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
