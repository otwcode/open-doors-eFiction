import os
import shutil
from configparser import ConfigParser
from logging import Logger
from pathlib import Path
from typing import List

from opendoors.mysql import SqlDb
from opendoors.big_insert import BigInsert
from opendoors.utils import (
    get_full_path,
    normalize,
    print_progress,
    make_banner,
    key_find,
    get_prefixed_path,
)


class EFictionChapters:
    """
    Process chapter contents and move them into the Open Doors working database.
    """

    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb = None):
        self.sql = sql
        self.config = config
        self.logger = logger
        self.working_original = self.config["Processing"]["simplified_original_db"]
        self.chapters_table = sql.read_table_to_dict(
            self.config["Processing"]["simplified_original_db"], "chapters"
        )
        self.working_open_doors = self.config["Processing"]["open_doors_working_db"]

    def _are_chapters_in_table(self) -> bool:
        return len([c for c in self.chapters_table if c["storytext"]]) > 0

    @staticmethod
    def __file_with_path(dirpath, subdir, filename):
        """
        Extract author_id and chapter_id from the story path
        :param dirpath: the path to the `stories` folder
        :param subdir: the subfolder in `stories`, ie the author id
        :param filename: the filename in `stories`, ie the chapter id
        :return: A dict containing metadata about the chapter based on its file path
        """
        return {
            "path": os.path.join(dirpath, filename),
            "chap_id": Path(filename).stem,
            "author_id": subdir,
        }

    def load_chapter_text_into_db(self, chapter_paths: List[dict]):
        """
        Load chapters text from the `stories` files into the chapters table. Checks for an encoding in the ini file and removes characters that are invalid in that encoding.
        :param chapter_paths: List of chapter metadata including path, author id and chapter id
        :return:
        """
        warnings = 0
        forced_continue = False
        self.logger.info("...loading data from chapters table...")
        old_chapters, current, total = self.sql.read_table_with_total(
            self.working_original, "chapters"
        )

        self.logger.info("...removing rows from existing chapters table...")
        self.sql.execute(self.working_open_doors, "TRUNCATE TABLE chapters;")

        self.logger.info("...loading text from chapter files...")
        insert_op = BigInsert(
            self.working_open_doors,
            "chapters",
            ["id", "position", "title", "text", "story_id", "notes"],
            self.sql,
        )
        try:
            encoding = self.config["Archive"]["encoding"]
        except KeyError:
            encoding = None
        if encoding is None:
            message_string = (
                """
You have not specified any character encoding in the config file! 

If you are unsure which encoding is used in the backup 
""".strip()
                + (
                    f""", please run the mojibake tool:

    mojibake {self.config['Archive']['chapter_path']}

    """
                    if shutil.which("mojibake") is not None
                    else f"""
, you can install the
mojibake tool from its repository:

    https://github.com/otwcode/open-doors-mojibake

follow the instructions in readme and then run it with this command:

    mojibake {self.config['Archive']['chapter_path']}

    """.strip()
                )
            )
            print(message_string)
            while encoding is None:
                encoding_text = input("Enter a valid encoding (press enter for utf8): ")
                if encoding_text == "":
                    encoding_text = "utf8"
                try:
                    # check if encoding is valid
                    "".encode(encoding_text)
                    encoding = encoding_text
                except LookupError:
                    print(f"{encoding_text} is not a valid encoding, try again")
        for old_chapter in old_chapters:
            chapid = old_chapter["chapid"]
            chapter = [
                chapter_path
                for chapter_path in chapter_paths
                if chapter_path["chap_id"] == str(chapid)
            ]
            if chapter:
                file = chapter[0]["path"]
                with open(file, "rb") as raw_chapter:
                    raw = raw_chapter.read()
                    while isinstance(raw, bytes):
                        try:
                            raw = raw.decode(encoding=encoding)
                        except UnicodeDecodeError as e:
                            error = f"Failed to decode {file}\n"
                            line_num = raw[: e.start].decode(encoding).count("\n")
                            error += f"At line {line_num}:\t{str(e)}\n"
                            error += (
                                "--\t"
                                + str(raw[max(e.start - 40, 0) : e.end + 30])
                                + "\n"
                            )
                            # print `^` under the offending byte
                            error += (
                                "\t"
                                + " "
                                * (len(str(raw[max(e.start - 40, 0) : e.start])) - 1)
                                + "^" * (len(str(raw[e.start : e.end])) - 3)
                                + "\n"
                            )
                            error += "Will be converted to:\n"
                            # remove the offending bytes (usually one)
                            raw = raw[: e.start] + raw[e.end :]
                            error += (
                                "++\t  "
                                + raw[max(e.start - 40, 0) : e.end + 30]
                                .decode(encoding, errors="ignore")
                                .replace("\n", "\\n")
                                .replace("\r", "\\r")
                                + "\n"
                            )
                            self.logger.warning(error)
                            warnings += 1
                    if warnings > len(old_chapters) * 0.3 and not forced_continue:
                        msg = f"""
A total of {warnings} automatic modifications have been performed so far!

It looks like something is VERY WRONG! Double check your selected character 
encoding. If you wish to continue the process, which is not recommended, type:
    
                            YES, DO AS I SAY!

In the prompt below, anything else will abort the process!
                        """.strip()
                        self.logger.error(msg)
                        if input(">>> ").strip() == "YES, DO AS I SAY!":
                            forced_continue = True
                            continue
                        else:
                            raise Exception("Process aborted, too many errors!")

                text = normalize(raw)
                if key_find("endnotes", old_chapter):
                    text = text + f"\n\n\n<hr>\n{old_chapter['endnotes']}"

                insert_op.addRow(
                    chapid,
                    old_chapter["inorder"],
                    old_chapter["title"],
                    text,
                    old_chapter["sid"],
                    old_chapter["notes"],
                )
            current = print_progress(current, total, "chapters converted")
        # If there were any errors, display a warning for the user to check the affected chapters
        if warnings >= 1:
            self.logger.warning(
                "If the character deletion is unacceptable please quit this processor and use the mojibake tool,"
                " then restart the processor from step 04"
            )
            self.logger.error(
                make_banner(
                    "-",
                    f"There were {warnings} warnings; check the affected chapters listed above to make sure curly quotes "
                    "and accented characters are correctly displayed.",
                )
            )
        insert_op.send()
        return self.sql.execute_and_fetchall(
            self.working_open_doors, "SELECT * FROM chapters;"
        )

    def list_chapter_files(self):
        """
        Retrieves information about the chapter files in the `stories` folder
        :return:
        """
        self.logger.info("Loading chapters from the filesystem...")
        chapter_paths = []
        for dirpath, dirnames, filenames in os.walk(
            get_full_path(self.config["Archive"]["chapter_path"])
        ):
            subdir = dirpath.split(os.path.sep)[-1]
            if (
                subdir
                and subdir
                != self.config["Archive"]["chapter_path"].split(os.path.sep)[-1]
            ):
                chapter_paths.extend(
                    [
                        self.__file_with_path(dirpath, subdir, filename)
                        for filename in filenames
                    ]
                )
        return chapter_paths

    def load_og_chapters_into_db(self):
        """
        Load chapters with text from the simplified db into the chapters table
        :return:
        """
        self.logger.info("...loading data from chapters table...")
        old_chapters, current, total = self.sql.read_table_with_total(
            self.working_original, "chapters"
        )

        self.logger.info("...removing rows from existing chapters table...")
        self.sql.execute(self.working_open_doors, "TRUNCATE TABLE chapters;")

        self.logger.info("...loading chapters from original chapters table...")
        insert_op = BigInsert(
            self.working_open_doors,
            "chapters",
            ["id", "position", "title", "text", "story_id", "notes"],
            self.sql,
        )

        for old_chapter in old_chapters:
            text = normalize(old_chapter["storytext"])
            if key_find("endnotes", old_chapter):
                text = text + f"\n\n\n<hr>\n{old_chapter['endnotes']}"

            insert_op.addRow(
                old_chapter["chapid"],
                old_chapter["inorder"],
                old_chapter["title"],
                text,
                old_chapter["sid"],
                old_chapter["notes"],
            )

            current = print_progress(current, total, "chapters converted")

        insert_op.send()
        return self.sql.execute_and_fetchall(
            self.working_open_doors, "SELECT * FROM chapters;"
        )

    def load_chapters(self, step_path: str):
        """
        Check if chapters are already present in the database and if not, load them from the filesystem
        :return:
        """
        if self._are_chapters_in_table():
            self.logger.info(
                "Chapters are already present in the original database, converting now"
            )
            self.load_og_chapters_into_db()
        else:
            if not self.config.has_option("Archive", "chapter_path"):
                chapter_path = input("Full path to chapter files\n>> ")
                self.config["Archive"]["chapter_path"] = os.path.normpath(chapter_path)

            chapter_paths = self.list_chapter_files()
            self.load_chapter_text_into_db(chapter_paths)

        database_dump = get_prefixed_path(
            "04", step_path, f"{self.working_open_doors}.sql"
        )
        self.logger.info(f"Exporting converted tables to {database_dump}...")
        self.sql.dump_database(self.working_open_doors, database_dump)
        return True
