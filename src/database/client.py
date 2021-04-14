import flask_login
from passlib.hash import sha256_crypt

from ..database import DataBase
from ..utils.decorateurs import sql_gestion_erreur


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
        return {'courriel': self.courriel, 'nom': self.nom, 'prenom': self.prenom, 'adresse': self.adresse,
                'artiste': False}

    def estArtiste(self):
        return False

    @flask_login.login_required
    def is_authenticated(self):
        return True

    def is_active(self):
        return True  # we have no concept of active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.courriel

    @staticmethod
    @sql_gestion_erreur
    def connection(courriel, mdp, curseur=DataBase.cursor()):
        curseur.execute('SELECT * FROM Client WHERE courriel=%s;', courriel)
        users = curseur.fetchone()
        if users is not None and \
                sha256_crypt.verify(mdp, users[1]):
            return Client(courriel, users[2], users[3], users[4])
        return None

    @staticmethod
    @sql_gestion_erreur
    def creer(courriel, mdp, nom, prenom, adresse, curseur=DataBase.cursor()):
        curseur.execute('INSERT INTO Client VALUE (%s, %s, %s, %s, %s);', (courriel, sha256_crypt.hash(mdp), nom, prenom, adresse))
        return Client(courriel=courriel, nom=nom, prenom=prenom, adresse=adresse)

    @staticmethod
    @sql_gestion_erreur
    def trouveAvecCourriel(courriel, curseur=DataBase.cursor()):
        curseur.execute("SELECT * FROM Client WHERE courriel=%s;", courriel)
        user = curseur.fetchone()
        return Client(user[0], user[2], user[3], user[4])
