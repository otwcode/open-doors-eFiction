import os
from configparser import ConfigParser
from logging import Logger
from pathlib import Path
from typing import List

from opendoors.mysql import SqlDb
from opendoors.utils import get_full_path, normalize, print_progress, make_banner


class EFictionChapters:
    """
    Process chapter contents and move them into the Open Doors working database.
    """
    def __init__(self, config: ConfigParser, logger: Logger, sql: SqlDb = None):
        self.sql = sql
        self.config = config
        self.logger = logger
        self.working_original = self.config['Processing']['simplified_original_db']
        self.chapters_table = sql.read_table_to_dict(self.config['Processing']['simplified_original_db'], "chapters")
        self.working_open_doors = self.config['Processing']['open_doors_working_db']

    def _are_chapters_in_table(self) -> bool:
        return len([c for c in self.chapters_table if c['storytext']]) > 0

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
            'path': os.path.join(dirpath, filename),
            'chap_id': Path(filename).stem,
            'author_id': subdir
        }

    def __load_chapter_text_into_db(self, chapter_paths: List[dict]):
        """
        Load chapters text from the `stories` files into the chapters table. Uses Windows 1252 if UTF-8 fails.
        :param chapter_paths: List of chapter metadata including path, author id and chapter id
        :return:
        """
        warnings = []
        self.logger.info("...loading data from chapters table...")
        old_chapters, current, total = self.sql.read_table_with_total(self.working_original, "chapters")

        self.logger.info("...removing rows from existing chapters table...")
        self.sql.execute(self.working_open_doors, "TRUNCATE TABLE chapters;")

        self.logger.info("...loading text from chapter files...")
        for old_chapter in old_chapters:
            chapid = old_chapter['chapid']
            chapter = [chapter_path for chapter_path in chapter_paths if chapter_path['chap_id'] == str(chapid)]
            if chapter:
                file = chapter[0]['path']
                try:
                    with open(file, 'r', encoding="utf-8") as f:
                        raw = f.read()
                except UnicodeDecodeError as err:
                    warnings.append(f"Chapter with id {chapid} contains non-ASCII characters which are not valid "
                                    f"UTF-8. Trying Windows 1252...")
                    with open(file, 'r', encoding='cp1252') as f:
                        raw = f.read()

                text = normalize(raw)
                if old_chapter['endnotes']:
                    text = text + f"\n\n\n<hr>\n{old_chapter['endnotes']}"

                query = """
                    INSERT INTO chapters (id, position, title, text, story_id, notes) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                """
                self.sql.execute(self.working_open_doors, query,
                                 (chapid, old_chapter['inorder'], old_chapter['title'], text,
                                  old_chapter['sid'], old_chapter['notes']))
            current = print_progress(current, total, "chapters converted")

        # If there were any errors, display a warning for the user to check the affected chapters
        if warnings:
            self.logger.warning("\n".join(warnings))
            self.logger.error(
                make_banner('-',
                            "There were warnings; check the affected chapters listed above to make sure curly quotes "
                            "and accented characters are correctly displayed."))
        return self.sql.execute_and_fetchall(self.working_open_doors, "SELECT * FROM chapters;")

    def __list_chapter_files(self):
        """
        Retrieves information about the chapter files in the `stories` folder
        :return:
        """
        self.logger.info("Loading chapters from the filesystem...")
        chapter_paths = []
        for dirpath, dirnames, filenames in os.walk(get_full_path(self.config['Archive']['chapter_path'])):
            subdir = dirpath.split(os.path.sep)[-1]
            if subdir and subdir != self.config['Archive']['chapter_path'].split(os.path.sep)[-1]:
                chapter_paths.extend([self.__file_with_path(dirpath, subdir, filename) for filename in filenames])
        return chapter_paths

    def load_chapters(self, step_path: str):
        """
        Check if chapters are already present in the database and if not, load them from the filesystem
        :return:
        """
        if self._are_chapters_in_table():
            self.logger.info("Nothing to do: chapters are already present in the original database")
            return True
        else:
            if not self.config.has_option('Archive', 'chapter_path'):
                chapter_path = input("Full path to chapter files\n>> ")
                self.config['Archive']['chapter_path'] = os.path.normpath(chapter_path)

            chapter_paths = self.__list_chapter_files()
            self.__load_chapter_text_into_db(chapter_paths)

        database_dump = os.path.join(step_path, f"{self.working_open_doors}.sql")
        self.logger.info(f"Exporting converted tables to {database_dump}...")
        self.sql.dump_database(self.working_open_doors, database_dump)
        return True
