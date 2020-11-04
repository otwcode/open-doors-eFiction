"""
Step 04
"""
from efiction.chapters import EFictionChapters
from opendoors.step_base import StepBase


class Step04(StepBase):
    """
    Step 4.
    """

    def run(self):
        """
        Run step 04
        """
        chapters = EFictionChapters(self.config, self.logger, self.sql)
        chapters.load_chapters()
        return self.finish()
