from pymysql import connect, Connection
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class DataBase:
    connection = connect(host=getenv('SQL_HOST'), user=getenv('SQL_USER'), password=getenv('SQL_PASSWORD'), db=getenv('SQL_DB'))

    @staticmethod
    def cursor():
        return DataBase.connection.cursor()
