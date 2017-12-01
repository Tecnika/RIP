import MySQLdb


class Connection:
    def __init__(self, host, db_name, read_default_file="~/.my.cnf"):
        self.host = host
        self.db_name = db_name
        self.read_default_file = read_default_file
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                db=self.db_name,
                read_default_file=self.read_default_file
            )
            return self.connection

    def disconnect(self):
        if self._connection:
            self._connection.close()