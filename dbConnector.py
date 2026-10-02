import psycopg2
import typing

class dbConnector:
    def __init__(self, dbName, userName, password, host="localhost", port=5432):
        self.dbName = dbName
        self.userName = userName
        self.password = password
        self.host = host
        self.port = port

        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(user=self.userName, password=self.password, host=self.host, port=self.port, database=self.dbName)

    def close(self):
        self.connection.close()

    def execute(self, query) -> typing.List[typing.Tuple] | None:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query)

        try:
            rows = cursor.fetchall()
        except:
            self.connection.commit()
            self.close()
            return []

        cursor.close()
        self.close()
        return rows
