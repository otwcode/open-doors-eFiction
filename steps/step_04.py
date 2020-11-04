"""
Step 04
"""
from efiction.chapters import EFictionChapters
from opendoors.step_base import StepBase


class Step04(StepBase):
    """
    Step 04. Load chapters into the Open Doors database.
    """

    def run(self):
        """
        Load chapter text into the `text` column in the chapters table and export a backup to the 04 folder.
        :return: True if this step was successful and can terminate, False if an error occurred
        """
        chapters = EFictionChapters(self.config, self.logger, self.sql)
        chapters.load_chapters(self.step_path)
        return self.finish()
