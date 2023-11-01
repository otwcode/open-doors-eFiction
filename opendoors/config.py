"""
Configuration for this Archive
"""
import configparser
import os
from logging import Logger

from opendoors.utils import get_full_path


class ArchiveConfig:
    """
    Wrapper for ConfigParser to provide convenience methods for configuration
    """

    def __init__(self, logger: Logger, code_name: str, working_dir: str):
        self.logger = logger
        self.working_dir = working_dir
        self.code_name = code_name
        self.config_path = os.path.join(self.working_dir, self.code_name + ".ini")
        self.config = self._create_or_get_archive_config()

    def _new_config_file(self):
        """
        Use sample config to generate a new config
        """
        self.config = configparser.ConfigParser()
        archive_config_path = os.path.join(os.getcwd(), "config_files")
        self.config.read(os.path.join(archive_config_path, "_sample_config.ini"))
        self._set_processing_config()
        self._set_archive_config()

        # Write out the new config file
        with open(self.config_path, "w") as configfile:
            self.config.write(configfile)
            self.logger.info(
                "Successfully created configuration file {}.".format(self.config_path)
            )
        return self.config

    def _set_archive_config(self):
        """
        Set Archive name and type
        """
        archive_name = input(
            "Full archive name (eg: 'TER/MA', 'West Wing Fanfiction Archive') - this will be used to "
            "generate dummy emails\n>> "
        )
        self.config["Archive"] = {
            "archive_name": archive_name,
            "archive_type": "EF",
            "code_name": self.code_name,
        }

    def _set_processing_config(self):
        """
        Set Processing settings
        """
        self.config["Processing"] = {
            "code_name": self.code_name,
            "working_dir": self.working_dir,
            "next_step": "01",
            "done_steps": "",
        }

    def _create_or_get_archive_config(self):
        config = configparser.ConfigParser()
        config_path = get_full_path(self.config_path)
        if os.path.exists(config_path):
            self.logger.info(f"Found existing config file {self.config_path}.")
            config.read(config_path)
        else:
            config = self._new_config_file()
        return config

    def processing(self, key):
        """
        Return value of the specified key from the Processing section in the ini file.
        :param key: Configuration key to look up.
        :return: The value of the specified key.
        """
        return self.config["Processing"][key]

    def archive(self, key):
        """
        Return value of the specified key from the Archive section in the ini file.
        :param key: Configuration key to look up.
        :return: The value of the specified key.
        """
        return self.config["Archive"][key]

    def save(self):
        """
        Save both the ini file kept in the working directory.
        :return: 0 if there is no config to save
        """
        if len(self.config.keys()) != 0:
            backup_path = os.path.join(
                self.processing("working_dir"), os.path.basename(self.config_path)
            )
            with open(backup_path, "w") as backup_config:
                self.config.write(backup_config)

            with open(self.config_path, "w") as configfile:
                self.config.write(configfile)
        else:
            return None
