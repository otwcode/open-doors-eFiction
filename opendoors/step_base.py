import os
import shutil
from abc import abstractmethod
from configparser import ConfigParser
from dataclasses import dataclass
from logging import Logger

from opendoors.mysql import SqlDb
from opendoors.utils import make_banner


@dataclass
class StepInfo():
    """
    Data class for steps.
    """
    step_number: str
    step_description: str
    next_step: str


class StepBase:
    """
    Base for processing steps.
    """

    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb, step_info: StepInfo):
        self.next_step = step_info.next_step
        self.sql = sql
        self.logger = logger
        self.config = config
        self.code_name = config['Archive']['code_name']
        self.step = step_info.step_number
        self.step_path = self.create_working_sub_dir()
        banner = make_banner('-', f'   Running Step {step_info.step_number}: {step_info.step_description}   ')
        self.logger.info(banner)

    def create_working_sub_dir(self):
        self.step_path = os.path.join(self.config['Processing']['working_dir'], self.step)
        if os.path.exists(self.step_path):
            shutil.rmtree(self.step_path)
            self.logger.info(f"Deleted existing {self.step} folder to start from scratch")
        os.makedirs(self.step_path)
        return self.step_path

    @abstractmethod
    def run(self):
        """
        Abstract method. Run the code for this step.
        """
        pass

    def finish(self):
        """
        Print a message about the end of the current step.
        :param current: The number of the step that has just finished.
        :param next: The number of the next step.
        """
        if self.next_step is None:
            self.logger.info("All steps completed.")
        else:
            self.logger.info(f"\nStep {self.step} completed, ready for step {self.next_step}\n")
            self.config['Processing']['next_step'] = self.next_step
        return True
