import flask_login
from ..database import DataBase


class Client:
    def __init__(self, courriel='', nom='', prenom='', adresse=''):
        self.courriel = courriel
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def copy(self, other):
        self.courriel = other.courriel
        self.nom = other.nom
        self.prenom = other.prenom
        self.adresse = other.adresse

    def getDict(self):
        return {'courriel': self.courriel, 'nom': self.nom, 'prenom': self.prenom, 'adresse': self.adresse, 'artiste': False}

    def estArtiste(self):
        return False

    @flask_login.login_required
    def is_authenticated(self):
        return True

    def is_active(self):
        return True # we have no concept of active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.courriel

    @staticmethod
    def trouveAvecCourriel(courriel):
        cursor = DataBase.cursor()
        cursor.execute('SELECT * FROM Client WHERE courriel=%s;',courriel)
        user = cursor.fetchone()
        return Client(user[0], user[2], user[3], user[4])

    @staticmethod
    def login(courriel, mdp):
        cursor = DataBase.cursor()
        cursor.execute('SELECT * FROM Client WHERE courriel=%s;',courriel)
        users = cursor.fetchone()
        if users is not None and users[1] == mdp:
            return Client(courriel, users[2], users[3], users[4])
        return None

    @staticmethod
    def register(courriel, mdp, nom, prenom, adresse):
        cursor = DataBase.cursor()
        cursor.execute('INSERT INTO Client VALUE (%s, %s, %s, %s, %s);',(courriel, mdp, nom, prenom, adresse))
        return Client(courriel=courriel, nom=nom, prenom=prenom, adresse=adresse)
