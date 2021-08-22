from .mysql import SqlDb
from tempfile import NamedTemporaryFile

class BigInsert:
    def __init__(self, database: str, table_name: str, columns: list, sql: SqlDb):
        """
        Handles `Load data local infile` inserts
        :param database: Name of database to use 
        :param table_name: Name of table to insert to 
        :param columns: list of column names, the order of those is used in addRow() 
            method
        :param sql: A connection to mysql to use
        """
        self._sql = sql
        self._sql.ensure_local_infile()
        self._database = database
        self._columns = columns
        self._tempfile = NamedTemporaryFile("w+")
        # We are storing data as a `tab separated` file
        # as tabs are just converted back into spaces
        # in HTML, we can just convert them here, instead of
        # some complicated escaping system
        self._query = f"""
            LOAD DATA LOCAL INFILE '{self._tempfile.name}'
            INTO TABLE {table_name}
            FIELDS TERMINATED BY '\t'
            LINES TERMINATED BY '\n'
            ({", ".join(columns)})
        """
        self._sql.logger.debug(f"Created BigInsert with query {self._query}")

    def addRow(self, *args):
        """
        Add row with data to be inserted, args must be in the same order as
        columns.
        :param *args: values to be inserted
        """
        if self._tempfile is None:
            raise Exception("Query was already sent")
        if len(args) != len(self._columns):
            raise Exception("Number of arguments does not equal number of columns!")
        # remove tabs and newlines
        values = [x.replace("\t", " ").replace("\n", " ") if isinstance(x, str) else str(x) for x in args]
        line = "\t".join(values) + "\n"
        self._tempfile.write(line)

    def send(self):
        """
        Perform insert operation and delete temporary file
        """
        self._tempfile.flush()
        self._sql.execute(self._database, self._query)
        self._tempfile.close()
        self._tempfile = None
        

