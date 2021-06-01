from unittest.mock import MagicMock

from efiction.metadata import EFictionMetadata
from opendoors.config import ArchiveConfig
from opendoors.mysql import SqlDb
from opendoors.utils import get_full_path


def create_efiction_converter(ini_file_name: str):
    """
    Create an EFictionConverter based on the supplied ini file
    :param ini_file_name: Name of ini file WITHOUT .ini extension
    :return: an EFictionConverter with the desired configuration
    """
    test_logger = MagicMock()
    test_config = ArchiveConfig(test_logger, ini_file_name, "efiction/tests/test_data").config
    test_sql = SqlDb(test_config, test_logger)
    test_config['Processing']['working_dir'] = get_full_path("efiction/tests/test_output")
    return EFictionMetadata(test_config, test_logger, test_sql, "test_path")


def load_fixtures(test_config, test_sql):
    dbs = [
        test_config['Processing']['open_doors_working_db'],
        test_config['Processing']['simplified_original_db'],
    ]
    for db in dbs:
        cursor = test_sql.conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {db.strip()};")
        test_sql.conn.commit()
    test_sql.load_sql_file_into_db(get_full_path(test_config['Processing']['original_tidied_file']))
