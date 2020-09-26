"""
Logging to console and file
"""
import logging
import os

import sys
from colorlog import ColoredFormatter


class Logging:
    """
    Utility class for logging
    """
    def __init__(self, working_dir, code_name):
        self.code_name = code_name
        self.working_dir = working_dir

    def logger(self):
        """
        Return a logger configured to write colour messages to the console and full log messages to a file in the
        working directory
        :return: an instance of the configured logger
        """
        log = logging.getLogger()
        log.setLevel(logging.INFO)

        color_formatter = ColoredFormatter('%(log_color)s%(message)s%(reset)s')
        stream = logging.StreamHandler(sys.stdout)
        stream.setLevel(logging.INFO)
        stream.setFormatter(color_formatter)
        log.addHandler(stream)

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fh = logging.FileHandler(os.path.join(self.working_dir, "{}.log".format(self.code_name)))
        fh.setFormatter(formatter)
        log.addHandler(fh)
        return log
