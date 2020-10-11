from unittest import TestCase

from opendoors.logging import Logging
from opendoors.utils import get_full_path


class LoggingTest(TestCase):
    def test_logger(self):
        logger = Logging(get_full_path("opendoors/tests/test_output"), "test").logger()
        handlers = logger.handlers
        self.assertEqual(20, logger.level, "log level should be INFO")
        self.assertEqual(6, len(handlers), "there should be 6 handlers in the Logger")

        file_handler = [h for h in handlers if h.__class__.__name__ == 'FileHandler'][0]
        formatter1 = file_handler.__dict__['formatter'].__dict__['_fmt']
        self.assertEqual("%(asctime)s %(levelname)s %(message)s",
                         formatter1,
                         "file formatter should include date, level and message only")

        stream_handler = [h for h in handlers if h.__class__.__name__ == 'StreamHandler'][0]
        formatter2 = stream_handler.__dict__['formatter'].__dict__['_fmt']
        self.assertEqual("%(log_color)s%(message)s%(reset)s",
                         formatter2,
                         "stream handler should use color formatting")
