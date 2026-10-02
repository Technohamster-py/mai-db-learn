from dbConnector import dbConnector
from db.queries import QUERY
from user import User
from conf import *

class DataController:
    def __init__(self, db_connector: dbConnector = None):
        self.db = db_connector if db_connector else dbConnector(DB_NAME, DB_USER, DB_PASSWORD)

    def setConnector(self, db_connector: dbConnector):
        self.db = db_connector

    def load_users(self):
        rows = self.db.execute(QUERY["all"])

        print(rows)

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