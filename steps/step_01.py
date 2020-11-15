"""
Step 01
"""
from efiction.original import EFictionOriginal
from opendoors.step_base import StepBase


class Step01(StepBase):
    """
    Load original database file into MySQL for future reference
    """

    def run(self):
        """
        Make a backup copy of the original database and convert it to a working set of tables for step 02
        :return: True if this step was successful and can move on to step 02, False if an error occurred
        """
        original = EFictionOriginal(self.config, self.logger, self.sql)
        original.load_original_file(self.step_path)
        return self.finish()
