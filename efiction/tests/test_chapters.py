import json
import copy
from unittest.mock import MagicMock, patch
import pytest


from efiction.chapters import EFictionChapters
from opendoors.big_insert import BigInsert
from opendoors.config import ArchiveConfig
from opendoors.mysql import SqlDb
from opendoors.utils import get_full_path, normalize, remove_output_files


def get_data():
    with open(get_full_path("efiction/tests/test_data/efiction_chapters.json"), "r", encoding="utf-8") as file:
        old_data_with_text = json.loads(file.read())
    old_data_no_text = copy.deepcopy(old_data_with_text)

    new_data_full = []
    new_data_missing = []
    for i, chap in enumerate(old_data_with_text):
        old_data_no_text[i]["storytext"] = ""

        text = normalize(chap['storytext'])
        if chap['endnotes']:
            text = text + f"\n\n\n<hr>\n{chap['endnotes']}"

        chap_dict = {
            "id": chap["chapid"],
            "position": chap["inorder"],
            "title": chap["title"],
            "text": text,
            "date": None,
            "story_id": chap["sid"],
            "notes": chap["notes"],
            "url": ""
        }
        new_data_full.append(chap_dict)

        # this is the chapter that fails due to wrong encoding
        if chap["chapid"] != 842:
            new_data_missing.append(chap_dict)

    return old_data_with_text, old_data_no_text, new_data_full, new_data_missing


old_data_with_text, old_data_no_text, new_data_full, new_data_missing = get_data()
test_logger = MagicMock()
test_config = ArchiveConfig(test_logger, "efiction", "efiction/tests/test_data").config


@pytest.fixture(scope='function', autouse=True)
def mock_sql():
    with patch('opendoors.mysql.SqlDb', autospec=True) as mock_Sql:
        sql = mock_Sql(test_config, test_logger)
        yield sql


@pytest.fixture(scope='function', autouse=True)
def mock_insert(mock_sql):
    with patch('efiction.chapters.BigInsert', autospec=True) as mock_Insert:
        insert = mock_Insert("efictiontest_working_open_doors", "chapters", ["id", "position", "title", "text", "story_id", "notes"], mock_sql)
        yield insert


@patch('efiction.chapters.EFictionChapters.load_og_chapters_into_db')
def test_chapters_with_text_main_method(mock_method, mock_sql, mock_insert):
    mock_sql.read_table_to_dict.return_value = old_data_with_text
    mock_sql.read_table_with_total.return_value = (old_data_with_text, 0, len(old_data_with_text))
    mock_sql.execute_and_fetchall.return_value = new_data_full

    efiction_chapters = EFictionChapters(test_config, test_logger, mock_sql)
    assert efiction_chapters.load_chapters("test_path"), "load_chapters doesn't return true"
    mock_method.assert_called_once()


def test_chapters_with_text_processing(mock_sql, mock_insert):
    mock_sql.read_table_to_dict.return_value = old_data_with_text
    mock_sql.read_table_with_total.return_value = (old_data_with_text, 0, len(old_data_with_text))
    mock_sql.execute_and_fetchall.return_value = new_data_full

    efiction_chapters = EFictionChapters(test_config, test_logger, mock_sql)
    working_chapters = efiction_chapters.load_og_chapters_into_db()
    assert len(new_data_full) == len(working_chapters), "Returned chapters from method don't match the number of expected chapters"

    mock_sql.read_table_to_dict.assert_called_with("efictiontest_test_step_original_efiction_edited", "chapters")
    mock_sql.read_table_with_total.assert_called_with("efictiontest_test_step_original_efiction_edited", "chapters")
    mock_sql.execute_and_fetchall.assert_called_with("efictiontest_working_open_doors", "SELECT * FROM chapters;")

    assert mock_insert.addRow.call_count == len(new_data_full), "addRow calls don't match the number of expected chapters"
    mock_insert.send.assert_called_once()


@patch('efiction.chapters.EFictionChapters.load_chapter_text_into_db')
def test_chapters_no_text_main_method(mock_method, mock_sql, mock_insert):
    mock_sql.read_table_to_dict.return_value = old_data_no_text
    mock_sql.read_table_with_total.return_value = (old_data_no_text, 0, len(old_data_no_text))
    mock_sql.execute_and_fetchall.return_value = new_data_missing

    efiction_chapters = EFictionChapters(test_config, test_logger, mock_sql)
    assert efiction_chapters.load_chapters("test_path"), "load_chapters doesn't return true"
    mock_method.assert_called_once()


def test_chapters_no_text_processing(monkeypatch, mock_sql, mock_insert):
    mock_sql.read_table_to_dict.return_value = old_data_no_text
    mock_sql.read_table_with_total.return_value = (old_data_no_text, 0, len(old_data_no_text))
    mock_sql.execute_and_fetchall.return_value = new_data_missing

    monkeypatch.setattr('builtins.input', lambda _: "YES, DO AS I SAY!")

    efiction_chapters = EFictionChapters(test_config, test_logger, mock_sql)
    working_chapters = efiction_chapters.load_chapter_text_into_db(efiction_chapters.list_chapter_files())
    assert len(new_data_missing) == len(working_chapters), "Returned chapters from method don't match the number of expected chapters"

    mock_sql.read_table_to_dict.assert_called_with("efictiontest_test_step_original_efiction_edited", "chapters")
    mock_sql.read_table_with_total.assert_called_with("efictiontest_test_step_original_efiction_edited", "chapters")
    mock_sql.execute_and_fetchall.assert_called_with("efictiontest_working_open_doors", "SELECT * FROM chapters;")

    assert mock_insert.addRow.call_count == len(new_data_missing), "addRow calls don't match the number of expected chapters"
    mock_insert.send.assert_called_once()
