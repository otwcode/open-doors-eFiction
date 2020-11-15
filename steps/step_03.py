"""
Step 03
"""
from efiction.metadata import EFictionMetadata
from opendoors.step_base import StepBase


class Step03(StepBase):
    """
    Step 03. Convert the eFiction data to a working Open Doors format and extract tags into a separate table.
    """

    def run(self):
        """
        Convert the tables to Open Doors format, export a backup to the 03 folder.
        :return: True if this step was successful and can move on to step 03, False if an error occurred
        """
        converter = EFictionMetadata(self.config, self.logger, self.sql, self.step_path)
        converter.convert_original_to_open_doors(self.step_path)
        return self.finish()
