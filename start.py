#!/usr/bin/python3
import atexit
import configparser

import sys

from opendoors import progress
from opendoors.config import ArchiveConfig
from opendoors.logging import Logging
from opendoors.mysql import SqlDb
from opendoors.step_base import StepInfo
from opendoors.utils import make_banner, set_working_dir
from steps import step_01, step_02, step_03, step_04

steps = {
    "01": {
        "info": StepInfo(
            next_step="02", step_description="Load original database", step_number="01"
        ),
        "class": step_01.Step01,
    },
    "02": {
        "info": StepInfo(
            next_step="03",
            step_description="Create simplified database",
            step_number="02",
        ),
        "class": step_02.Step02,
    },
    "03": {
        "info": StepInfo(
            next_step="04",
            step_description="Convert metadata to Open Doors tables",
            step_number="03",
        ),
        "class": step_03.Step03,
    },
    "04": {
        "info": StepInfo(
            next_step="None",
            step_description="Load chapters into Open Doors tables",
            step_number="04",
        ),
        "class": step_04.Step04,
    },
}

config = configparser.ConfigParser()


@atexit.register
def save_config_and_exit():
    """
    Save config on exit
    """
    print("Saving config...")
    config.save()


if __name__ == "__main__":
    """
    Syntax: python3 start.py [CODENAME] [ROOT_PATH_TO_USE]
    Example: python3 start.py mvw /users/me/otw_opendoors
    Prompts user if no codename is given, and uses an "otw_opendoors" in the user's home directory if no root path given
    """
    if len(sys.argv) > 1:
        code_name = sys.argv[1]
    else:
        code_name = None
        while code_name == None or any(  # noqa: E711
            [x not in "qwertyuiopasdfghjklzxcvbnm" for x in code_name]
        ):
            code_name = input(
                "Please provide a short, lowercase code name with no spaces or punctuation for the archive "
                "you are processing (and make a note of it as you'll need it in future!):\n>> "
            )

    banner_text = f"""Starting processing for archive "{code_name}"..."""
    banner = make_banner("=", banner_text)

    path = sys.argv[2] if len(sys.argv) > 2 else None
    working_dir = set_working_dir(path, code_name)

    logger = Logging(working_dir, code_name).logger()
    logger.info(banner)

    config = ArchiveConfig(logger, code_name, working_dir)
    archive_config = config.config

    sql = SqlDb(archive_config, logger)

    progress.continue_from_last(archive_config, logger, sql, steps)
