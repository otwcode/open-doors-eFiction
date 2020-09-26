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
    :return:
    """
    return join(path) if Path(path).is_absolute() else join(ROOT_DIR, path)


def make_banner(border_char: chr, banner_text: str, padding=2):
    """
    Make a banner with the provided text bordered by the provided character
    :param border_char: The character to use for the top and bottom border.
    :param banner_text: The text to display in the banner, including any leading
    :param padding: Optional. The number of spaces to put on either side of the text.
    :return:
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
    :return:
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
