import sys


def make_banner(border_char, banner_text):
    banner_border = border_char.ljust(len(banner_text), border_char)
    return f"\n{banner_border}\n{banner_text}\n{banner_border}"


if __name__ == '__main__':
    """
    Syntax: python3 start.py CODENAME ROOT_PATH_TO_USE
    Example: python3 start.py mvw /users/me/otw_opendoors
    Prompts user if no codename is given, and uses an "otw_opendoors" in the user's home directory if no root path given
    """
    if len(sys.argv) > 1:
        code_name = sys.argv[1]
    else:
        code_name = input(
            "Please provide a short, lowercase code name with no spaces or punctuation for the archive "
            "you are processing (and make a note of it as you'll need it in future!):\n>> ")

    banner_text = f"""Starting processing for archive "{code_name}"..."""
    banner = make_banner('=', banner_text)

