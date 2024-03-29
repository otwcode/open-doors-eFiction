"""
Static utilities for use throughout
"""
import glob
import html
import os
import re
import shutil
from typing import Mapping
from pathlib import Path

import unicodedata


def get_full_path(path):
    """
    Return the absolute path based on the supplied fragment
    :param path: A relative path fragment. If this is already the absolute path, just return it.
    :return: The absolute path.
    """
    full_path: Path = Path(path).resolve(strict=False)
    return str(full_path)


def copy_to_dir(old_file_path, new_file_dir, new_file_name):
    """
    Copy the source file to the destination path and filename
    :param old_file_path: The full path to the file to copy.
    :param new_file_dir: The full path to the destination directory.
    :param new_file_name: The new name of the file.
    :return:
    """
    Path(new_file_dir).mkdir(parents=True, exist_ok=True)
    return shutil.copyfile(old_file_path, os.path.join(new_file_dir, new_file_name))


def check_if_file_exists(config, section, option):
    """
    Check if the specified config option exists and is a valid, existing path
    :param config: The configuration for the current archive.
    :param section: The section containing the configuration option. E.g.: "Processing"
    :param option: The option containing the file path to check. E.g.: "backup_file"
    :return: True if the specified configuration exists and is a valid path, False if not.
    """
    return config.has_option(section, option) and Path(config[section][option]).exists


def key_find(
    needle: object, haystack: Mapping[object, object], none_val: object = None
) -> object:
    """
    Helper function to search a Dict (or any Mappable type) for a key, returning
    the value if it exists. This avoids KeyErrors when it is not certain if the key
    exists in the array or not.
    :param needle: The key to return, if it exists
    :param haystack: The Dict/Mappable to search
    :return The value if the key is in the haystack, or none_val if not
    """

    # On occasion, we may get literal None's returned for a value instead of the
    # key being missing.  Make sure to treat those as failures.
    if needle in haystack and haystack[needle] is not None:
        return haystack[needle]
    return none_val


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
    return (
        f"\n{banner_border}\n"
        f"{' ' * padding}{banner_text}{' ' * padding}\n"
        f"{banner_border}"
    )


def set_working_dir(path=None, code_name=""):
    """
    Use provided path or prompt user to accept or change default path. Note that output is to console, not log file as
    the logger isn't initialised until there is a working directory.
    :param path: Optional. The complete path including archive code name to use as a working directory.
    :param code_name: Optional. The short code name for the archive. Ignored if `path` is provided.
    :return: The new working directory.
    """
    if path is None:
        _working_dir = os.path.join(os.path.expanduser("~"), "otw_opendoors", code_name)
        prompt = input(
            "Path to working directory to use for this archive "
            "(press Enter for default: {}):\n>> ".format(_working_dir)
        )
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

    sys.stdout.write(f"\r{current}/{total} {text}")
    if current >= total:
        sys.stdout.write("\n")
    sys.stdout.flush()
    return current


def remove_output_files(path: str):
    """
    Remove all files and folders in a path - mainly useful for test cleanup
    :param path: the path to tidy up, relative to the root of the project
    """
    filtered = [f for f in glob.glob(path) if not re.match(r"\.keep", f)]
    for file in filtered:
        try:
            if Path(file).is_dir():
                shutil.rmtree(file)
            else:
                os.remove(file)
        except PermissionError:
            # We don't necessarily care that much
            continue


def normalize(text):
    """
    Unescape HTML and convert unicode entities into the corresponding character
    :param text: the text to normalize
    :return: normalized, unescaped text
    """
    return unicodedata.normalize("NFKD", html.unescape(text) or "").strip()


def get_prefixed_path(step: str, path: str, filename: str = ""):
    """
    Adds the efiction step prefix to filenames or folders
    :param step: The current step
    :param path: The base path
    :param filename: The file name. If left null, default is to create new folder
    :return: The path with the efiction prefix added as a folder or to a file name.
    """
    prefix = f"efiction-{step}"
    if filename:
        return os.path.join(path, f"{prefix}-{filename}")
    else:
        return os.path.join(path, prefix)
