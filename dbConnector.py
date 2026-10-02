import typing

import psycopg2


class dbConnector:
    def __init__(self, dbName, userName, password, host="localhost", port=5432):
        self.dbName = dbName
        self.userName = userName
        self.password = password
        self.host = host
        self.port = port

        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            user=self.userName,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.dbName,
        )

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute(self, query, params=None) -> typing.List[typing.Tuple]:
        """
        @brief Выполняет SQL-запрос и возвращает результат.
        @details Параметры передаются отдельно от SQL-запроса, что позволяет использовать параметризованные запросы.
        """

        self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)

                if cursor.description is None:
                    self.connection.commit()
                    return []

                return cursor.fetchall()
        finally:
            self.close()