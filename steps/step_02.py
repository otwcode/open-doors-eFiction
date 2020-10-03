"""
Step 02
"""
from efiction.simplified import EFictionSimplified
from opendoors.step_base import StepBase


class Step02(StepBase):
    """
    Step 02.
    """

    def run(self):
        """
        Run step 02
        """
        converter = EFictionSimplified(self.config, self.logger, self.sql)
        converter.simplify_original_file(self.step_path)
        return self.finish()
