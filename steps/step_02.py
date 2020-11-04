"""
Step 02
"""
from efiction.simplified import EFictionSimplified
from opendoors.step_base import StepBase


class Step02(StepBase):
    """
    Step 02. Remove unwanted eFiction tables and rename them to remove the eFiction prefix.
    """

    def run(self):
        """
        Simply the database and create a backup in the 02 folder.
        :return: True if this step was successful and can move on to step 03, False if an error occurred
        """
        converter = EFictionSimplified(self.config, self.logger, self.sql)
        converter.simplify_original_file(self.step_path)
        return self.finish()
