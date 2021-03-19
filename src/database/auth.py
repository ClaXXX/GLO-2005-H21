from flask import session
from src.database.client import Client


class Auth:
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password

    def login(self, cursor):
        cursor.execute('SELECT * FROM Utilisateurs WHERE courriel=' + self.mail + ';')
        users = cursor.fetchone()
        print(users)
        if users is not None and users[1] == self.password:
            return Client(self.mail, users[2], users[3])
        return None
