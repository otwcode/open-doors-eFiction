from opendoors.utils import get_full_path


def load_fixtures(test_config, test_sql):
    dbs = [
        test_config['Processing']['open_doors_working_db'],
    ]
    for db in dbs:
        cursor = test_sql.conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {db.strip()};")
        test_sql.conn.commit()
    test_sql.load_sql_file_into_db(get_full_path("efiction/tests/test_data/efiction_filtered.sql"))
