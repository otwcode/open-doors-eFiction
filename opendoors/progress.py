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
    def __is_valid(s):
        return s not in [',', '', ' ']

    run_next = True
    next_step = config['Processing']['next_step'] if config['Processing']['next_step'] else "01"
    while run_next:
        done_steps = set(filter(__is_valid, config['Processing']['done_steps'].split(",")))
        print(next_step)
        if next_step != "None":
            step_to_run = get_next_step(config, next_step, list(done_steps))
            step_config = steps[step_to_run]
            step = step_config['class'](config, logger, sql, step_config['info'])
            run_next = step.run()
            if run_next:
                next_step = config['Processing']['next_step'] = step.next_step
                if len(done_steps) == 0:
                    done_steps = {step_to_run.strip()}
                else:
                    done_steps.add(step_to_run.strip())
                print(f"{done_steps} = {len(done_steps)}")
                config['Processing']['done_steps'] = ', '.join(done_steps)
        else:
            restart_yn = input(f"All steps have been completed for this archive. Do you want to\n"
                               "1. Restart from step 1\n"
                               "2. Exit (default - press Enter)\n>> ")
            if restart_yn == "1":
                next_step = "01"
            else:
                run_next = False


def get_next_step(config, step_to_run, completed_steps):
    """
    Prompt to restart from scratch or continue with the next step in the sequence
    :param config: The config for the current archive.
    :param step_to_run: The next step in the process.
    :param completed_steps: The steps already completed.
    :return:
    """
    if step_to_run != "01" and completed_steps:
        if len(completed_steps) > 1:
            done_steps = "Steps {} and {} have".format(", ".join(completed_steps[:-1]), completed_steps[-1])
        elif len(completed_steps) == 1:
            done_steps = "Step {} has".format(", ".join(completed_steps))
        else:
            done_steps = "No steps"
        resume_yn = \
            input(f"{done_steps} been completed. Please choose one of the following options:\n"
                  f"1. Restart entire process from step 01 (this will remove any working files already created)"
                  f"2. Continue processing from step {step_to_run} (default - press enter)\n>> ")
        resume = resume_yn.lower() != '1'
    else:
        resume = True
    if not resume:
        step_to_run = "01"
    return step_to_run
