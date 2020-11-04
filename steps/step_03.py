"""
Step 03
"""
from efiction.metadata import EFictionMetadata
from opendoors.step_base import StepBase


class Step03(StepBase):
    """
    Step 03.
    """

    def run(self):
        """
        Run step 03
        """
        converter = EFictionMetadata(self.config, self.logger, self.sql)
        converter.convert_original_to_open_doors()
        return self.finish()
