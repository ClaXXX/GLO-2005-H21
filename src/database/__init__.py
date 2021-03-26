from pymysql import connect


class DataBase:
    def __init__(self, host, user, password, db):
        self.connection = connect(host=host, user=user, passwd=password, db=db,autocommit = True)

    def cursor(self):
        return self.connection.cursor()
