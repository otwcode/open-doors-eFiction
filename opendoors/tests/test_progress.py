from unittest import TestCase
from unittest.mock import patch, MagicMock

from opendoors.config import ArchiveConfig
from opendoors.progress import continue_from_last, update_done_steps, get_next_step
from opendoors.step_base import StepBase, StepInfo
from opendoors.utils import remove_output_files


class Step1(StepBase):
    """Test Step 1"""

    def run(self):
        """Run Test Step 1"""
        return True


class Step2(StepBase):
    """Test Step 2"""

    def run(self):
        """Run Test Step 2"""
        return True


steps = {
    "01": {
        "info": StepInfo(next_step="02", step_description="Step 1", step_number="01"),
        "class": Step1,
    },
    "02": {
        "info": StepInfo(next_step="None", step_description="Step 2", step_number="02"),
        "class": Step2,
    },
}

test_logger = MagicMock()
test_sql = MagicMock()


class TestProgress(TestCase):
    def tearDown(self) -> None:
        """Remove any files generated in test_output"""
        remove_output_files("opendoors/tests/test_output/*")

    # This patch responds '2' to every prompt and makes it run all the steps in turn
    @patch("builtins.input", lambda *args: "2")
    def test_continue_from_last(self):
        test_config = ArchiveConfig(
            test_logger, "test1", "opendoors/tests/test_output"
        ).config
        continue_from_last(test_config, test_logger, test_sql, steps)
        self.assertSetEqual(
            set("01, 02".split(", ")),
            set(test_config["Processing"]["done_steps"].split(", ")),
            "continue_from_last should update the done_steps config",
        )

    @patch("builtins.input", lambda *args: "Full Archive Name")
    def test_update_done_steps(self):
        test_config = ArchiveConfig(
            test_logger, "test2", "opendoors/tests/test_output"
        ).config
        test_config["Processing"]["done_steps"] = "01, 02"
        done_steps = update_done_steps(test_config, ["01", "02"], "03")
        self.assertEqual(
            "01, 02, 03",
            done_steps,
            "update_done_steps should return the done steps as a string",
        )

    @patch("builtins.input", lambda *args: "2")
    def test_get_next_step_after_01(self):
        test_config = ArchiveConfig(
            test_logger, "test3", "opendoors/tests/test_output"
        ).config
        next_step, done_steps = get_next_step(test_config, "01")
        self.assertEqual("01", next_step, "next_step should be set to 01")
        self.assertEqual([], done_steps, "done_steps should be reset to empty")

    @patch("builtins.input", lambda *args: "2")
    def test_get_next_step_after_02(self):
        test_config = ArchiveConfig(
            test_logger, "test4", "opendoors/tests/test_output"
        ).config
        test_config["Processing"]["done_steps"] = "01, 02"
        next_step, done_steps = get_next_step(test_config, "02")
        self.assertEqual("02", next_step, "next_step should be set to 02")
        self.assertListEqual(
            test_config["Processing"]["done_steps"].split(", "),
            done_steps,
            "done_steps should be the value currently in the config",
        )

    @patch("builtins.input", lambda *args: "1")
    def test_get_next_step_with_restart(self):
        test_config = ArchiveConfig(
            test_logger, "test5", "opendoors/tests/test_output"
        ).config
        test_config["Processing"]["done_steps"] = "01, 02"
        next_step, done_steps = get_next_step(test_config, "02")
        self.assertEqual("01", next_step, "next_step should be set to 01")
        self.assertEqual([], done_steps, "done_steps should be reset to empty")
