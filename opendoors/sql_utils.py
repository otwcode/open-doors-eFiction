import os
import re
from collections import defaultdict
from itertools import groupby

import sqlparse


def extract_table_name(sql: str):
    """
    Extracts table names from common SQL statements
    :param sql: str. a single SQL statement
    :return:
    """
    prefixes = ["drop table if exists ", "create table ", "insert into "]
    end = re.sub(r"|".join(map(re.escape, prefixes)), "", sql.lower().strip())
    table_name_match = re.match(r"`?(\S*?_?\S*?)`?[\s;]", end)
    table_name = (
        str.strip(table_name_match[1]).replace("`", "")
        if table_name_match is not None
        else ""
    )
    return table_name


def group_by_table(statements: list):
    """
    Group SQL statements into a dictionary keyed by the table they affect (only works for single-table statements)
    :param statements: list of SQL statements
    :return: dict of statements grouped by table name
    """
    group_list = [
        (gr, list(items)) for gr, items in groupby(statements, key=extract_table_name)
    ]
    groups = defaultdict(list)
    for gr, stmt_list in group_list:
        groups[gr].extend(stmt_list)
    return groups


def add_create_database(database_name: str, statements: list):
    """
    Add drop, create and use database commands to the start of a list of statements
    :param database_name: database to drop/create
    :param statements: existing SQL statements to apply to that database
    :return: amended list of statements
    """
    return [
        f"DROP DATABASE IF EXISTS `{database_name}`;",
        f"CREATE DATABASE `{database_name}`;",
        f"USE `{database_name}`;\n",
    ] + statements


def write_statements_to_file(filepath: str, statements: list) -> str:
    """
    Write the contents of statements to the specified file path.
    :param filepath: full path to the desired output file
    :param statements: list of strings to write to the output file
    :return: the output path
    """
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    with open(filepath, "w", encoding="utf-8") as file:
        for statement in statements:
            if statement.startswith("DROP TABLE"):
                file.write("\n")
            file.write(statement + "\n")
    return filepath


def parse_remove_comments(original_db_sql: str):
    """
    Remove comments and split into separate statements
    :param original_db_sql: SQL statements
    :return: list of statements without comments
    """
    stmts = sqlparse.format(original_db_sql, None, strip_comments=True)
    raw_statements = sqlparse.split(stmts)
    cleaned_statements = [
        clean_up_sql_statement(item)
        for item in raw_statements
        if item not in [";", "#"]
    ]
    return [statement for statement in cleaned_statements if statement.strip()]


def remove_invalid_date_default(statement: str) -> str:
    """
    Replace datetime column definitions which are invalid in MySQL 5.7.
    :param statement: SQL statement to modify
    :return: modified statement
    """
    return re.sub(
        r"datetime not null default '0000-00-00 00:00:00'",
        "datetime DEFAULT NULL",
        statement,
        flags=re.IGNORECASE,
    )


def remove_unwanted_statements(statement: str) -> str:
    """
    Remove database creation and use statements so we can replace them with new ones, and remove other miscellaneous
    statements we don't need.
    :param statement: SQL statement to modify
    :return: an empty string if this was a CREATE or USE DATABASE statement or the original statement if not
    """
    if statement.lower().startswith(("create database ", "use ", "lock ", "unlock ")):
        return ""
    else:
        return statement


def clean_up_sql_statement(statement: str) -> str:
    """
    Chain other cleanup methods for tidiness
    :param statement: original statement to modify
    :return: modified statement
    """
    return remove_unwanted_statements(remove_invalid_date_default(statement))
