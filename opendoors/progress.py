import traceback
from configparser import ConfigParser
from logging import Logger

from opendoors.mysql import SqlDb


def continue_from_last(config: ConfigParser, logger: Logger, sql: SqlDb, steps: dict):
    """
    Start the next step in the process
    :param config: The config for the current archive.
    :param logger: The logger used for this import.
    :param sql: The SqlDb instance used for this import.
    :param steps: A dict containing all the steps in this process as StepInfo items.
    """
    run_next = True
    next_step = (
        config["Processing"]["next_step"] if config["Processing"]["next_step"] else "01"
    )
    try:
        while run_next:
            if next_step != "None":
                # Prompt for the step to run based on the configured next step
                step_to_run, done_steps = get_next_step(config, next_step)
                step_config = steps[step_to_run]
                step = step_config["class"](config, logger, sql, step_config["info"])
                run_next = step.run()

                # Update the list of completed steps in the config
                if run_next:
                    next_step = config["Processing"]["next_step"] = step.next_step
                    update_done_steps(config, done_steps, step_to_run)
            else:
                restart_yn = input(
                    "All steps have been completed for this archive. Do you want to\n"
                    "1. Restart from step 1\n"
                    "2. Exit (default - press Enter)\n>> "
                )
                if restart_yn == "1":
                    next_step = "01"
                else:
                    run_next = False
    except Exception:
        logger.error(traceback.format_exc())


def update_done_steps(config: ConfigParser, done_steps: list, step_to_run: str) -> str:
    """
    Update the list of completed steps in the config.
    :rtype: str
    :param config: The configuration for the current archive.
    :param done_steps: Current list of completed steps.
    :param step_to_run: The step that has just been completed.
    :return: The new configuration value for done_steps.
    """
    if len(done_steps) == 0:
        done_steps = {step_to_run.strip()}
    else:
        done_steps.append(step_to_run.strip())
    steps = config["Processing"]["done_steps"] = ", ".join(done_steps)
    return steps


def get_next_step(config: ConfigParser, step_to_run: str) -> (str, list):
    """
    Prompt to restart from scratch or continue with the next step in the sequence
    :param config: The config for the current archive.
    :param step_to_run: The next step in the process.
    :return:
    """

    def __is_valid(s):
        return s not in [",", "", " "]

    def __tidy_steps():
        return sorted(
            set(
                list(
                    map(
                        lambda x: x.strip(),
                        filter(
                            __is_valid, config["Processing"]["done_steps"].split(",")
                        ),
                    )
                )
            )
        )

    completed_steps = [] if step_to_run == "01" else __tidy_steps()
    if step_to_run != "01" and completed_steps:
        if len(completed_steps) > 1:
            steps_list = "Steps {} and {} have".format(
                ", ".join(completed_steps[:-1]), completed_steps[-1]
            )
        elif len(completed_steps) == 1:
            steps_list = "Step {} has".format(", ".join(completed_steps))
        else:
            steps_list = "No steps have"
        resume_yn = input(
            f"{steps_list} been completed. Please choose one of the following options:\n"
            f"1. Restart entire process from step 01 (this will remove any working files already created)\n"
            f"2. Continue processing from step {step_to_run} (default - press enter)\n>> "
        )
        restart = resume_yn.lower() == "1"
    else:
        restart = False
    if restart:
        step_to_run = "01"
        completed_steps = []
    return step_to_run, completed_steps
