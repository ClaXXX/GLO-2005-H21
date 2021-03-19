from pymysql import connect
from os import getenv


def setup():
    mydb = connect(
        host=getenv('SQL_HOST'),
        user=getenv('SQL_USER'),
        password=getenv('SQL_PASSWORD')
    )
    with open('commandes.sql', 'r') as f:
        with mydb.cursor() as cursor:
            cursor.execute(f.read(), multi=True)
        mydb.commit()
