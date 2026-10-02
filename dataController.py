from dbConnector import dbConnector
from db.queries import QUERY
from user import User
from conf import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class DataController:
    def __init__(self, db_connector: dbConnector = None):
        self.db = db_connector if db_connector else dbConnector(
            DB_NAME,
            DB_USER,
            DB_PASSWORD,
            DB_HOST,
            DB_PORT,
        )

    def setConnector(self, db_connector: dbConnector):
        self.db = db_connector

    def load_users(self):
        """
        @brief Загружает все записи телефонной книги.
        @details Результат SQL-запроса преобразуется в список объектов User.
        """

        rows = self.db.execute(QUERY["all"])

        return [
            User(
                last_name=row[0],
                first_name=row[1],
                surname=row[2],
                phone=row[3],
                street_address=row[4],
                house=row[5],
                building=row[6],
                apartment=row[7],
            )
            for row in rows
        ]

    def load_firstnames(self):
        """
        @brief Загружает список имён.
        """

        return [row[0] for row in self.db.execute(QUERY["firstnames"])]

    def load_lastnames(self):
        """
        @brief Загружает список фамилий.
        """

        return [row[0] for row in self.db.execute(QUERY["lastnames"])]

    def load_surnames(self):
        """
        @brief Загружает список отчеств.
        """

        return [row[0] for row in self.db.execute(QUERY["surnames"])]

    def load_streets(self):
        """
        @brief Загружает список улиц.
        """

        return [row[0] for row in self.db.execute(QUERY["streets"])]

    def search_users(
        self,
        first_name=None,
        last_name=None,
        surname=None,
        street=None,
        phone=None,
    ):
        """
        @brief Выполняет поиск пользователей по заданным параметрам.
        @details Все заданные параметры объединяются условием AND. Пустые параметры игнорируются.
        """

        query = """
            SELECT
                lastnames.lastname,
                firstnames.firstname,
                surnames.surname,
                main.tel,
                streets.street,
                main.building,
                main.building_k,
                main.apartment
            FROM main
            LEFT JOIN lastnames ON main.lastname = lastnames.id
            LEFT JOIN firstnames ON main.firstname = firstnames.id
            LEFT JOIN surnames ON main.surname = surnames.id
            LEFT JOIN streets ON main.street = streets.id
        """

        conditions = []
        params = []

        if first_name:
            conditions.append("firstnames.firstname = %s")
            params.append(first_name)

        if last_name:
            conditions.append("lastnames.lastname = %s")
            params.append(last_name)

        if surname:
            conditions.append("surnames.surname = %s")
            params.append(surname)

        if street:
            conditions.append("streets.street = %s")
            params.append(street)

        if phone:
            conditions.append("main.tel = %s")
            params.append(phone)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        rows = self.db.execute(query, tuple(params))

        return [
            User(
                last_name=row[0],
                first_name=row[1],
                surname=row[2],
                phone=row[3],
                street_address=row[4],
                house=row[5],
                building=row[6],
                apartment=row[7],
            )
            for row in rows
        ]