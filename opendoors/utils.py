"""
Static utilities for use throughout
"""
import os
from os.path import join
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def get_full_path(path):
    """
    Return the absolute path based on the supplied fragment
    :param path: A relative path fragment. If this is already the absolute path, just return it.
    :return: The absolute path.
    """
    return join(path) if Path(path).is_absolute() else join(ROOT_DIR, path)


def make_banner(border_char: chr, banner_text: str, padding=2):
    """
    Make a banner with the provided text bordered by the provided character
    :param border_char: The character to use for the top and bottom border.
    :param banner_text: The text to display in the banner, including any leading
    :param padding: Optional. The number of spaces to put on either side of the text.
    :return: The bannered string.
    """
    width = len(banner_text) + (padding * 2)
    banner_border = border_char.ljust(width, border_char)
    return f"\n{banner_border}\n" \
           f"{' ' * padding}{banner_text}{' ' * padding}\n" \
           f"{banner_border}"


def set_working_dir(path=None, code_name=""):
    """
    Use provided path or prompt user to accept or change default path
    :param path: Optional. The complete path including archive code name to use as a working directory.
    :param code_name: Optional. The short code name for the archive. Ignored if `path` is provided.
    :return: The new working directory.
    """
    if path is None:
        _working_dir = os.path.join(os.path.expanduser("~"), "otw_opendoors", code_name)
        prompt = input("Path to working directory to use for this archive "
                       "(press Enter for default: {}):\n>> ".format(_working_dir))
        if prompt != "":
            _working_dir = prompt
    else:
        _working_dir = path

    try:
        if os.path.exists(_working_dir):
            print("Found existing working directory {}".format(_working_dir))
        else:
            os.makedirs(_working_dir)
            print("Successfully created the directory {}".format(_working_dir))

    except OSError as err:
        print("Creation of the directory {} failed: {}".format(_working_dir, err))
        return False
    else:
        return _working_dir


def print_progress(current, total, text="stories"):
    """
    Print constantly updating progress text to the command line, in the form `current/total item_name`. Note that this
    increments current, so no need to do that in the calling code.
    :param current: current number
    :param total: total number
    :param text: text to display after the counters
    :return: updated progress text on the same line as the previous print out
    """
    current += 1
    import sys
    sys.stdout.write(f'\r{current}/{total} {text}')
    if current >= total:
        sys.stdout.write("\n")
    sys.stdout.flush()
    return current
