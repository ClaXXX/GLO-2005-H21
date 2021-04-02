from src.database.client import Client

# TODO: Amerliorer l'ajout avec un minimum de parsing
class Auth:
    def __init__(self, courriel, mdp):
        self.courriel = courriel
        self.mdp = mdp

    def login(self, cursor):
        cursor.execute("SELECT * FROM Client WHERE courriel=" + self.courriel + ";")
        users = cursor.fetchone()
        if users is not None and users[1] == self.mdp:
            return Client(self.mdp, users[2], users[3])
        return None

    def register(self, cursor, client):
        cursor.execute("INSERT INTO Client VALUE (" + self.courriel + "," + self.mdp
                       + "," + client.nom + "," + client.prenom + "," + client.adresse + ");")
