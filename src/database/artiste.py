import copy

from src.database import DataBase
from src.database.client import Client


class Artiste(Client):
    def __init__(self, client, nom):
        super().__init__()
        self.copy(client)
        self.nomArtiste = nom

    def getDict(self):
        d = super().getDict()
        d['nomArtiste'] = self.nomArtiste
        d['artiste'] = True
        return d

    def estArtiste(self):
        return True

    @staticmethod
    def trouveAvecCourriel(courriel):
        cursor = DataBase.cursor()
        cursor.execute("SELECT * FROM Artiste WHERE courriel=" + courriel + ";")
        artiste = cursor.fetchone()
        if artiste is not None:
            return Artiste(Client.trouveAvecCourriel(courriel), artiste[1])
        return None

    @staticmethod
    def devient_artiste(courriel, nom):
        client = Client.trouveAvecCourriel(courriel)
        if client is None:
            return None
        cursor = DataBase.cursor()
        cursor.execute("INSERT INTO Artiste VALUE (" + courriel + ",'" + nom + "');")
        return Artiste(client, nom)

    def toDict(self):
        return {'courriel': self.courriel,'nom': self.nom}

    @staticmethod
    def cherche_nom(nom,curseur):
        curseur.execute('SELECT * FROM Artiste WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return {'nom': resultat[1], 'courriel': resultat[0]}
        return None

    @staticmethod
    def liste_artiste(curseur):
        curseur.execute('SELECT * FROM Artiste;')
        resultat = curseur.fetchall()

        if resultat is not None:
            artistes = [Artiste.cherche_nom(x[1], curseur) for x in resultat]
            return artistes
        return None

    @staticmethod
    def recherche(nom, curseur):
        nom = '%' + nom + '%'
        curseur.execute('SELECT * FROM Artiste WHERE nom  LIKE %s ;', nom)
        resultat = curseur.fetchall()
        if resultat is not None:
            return [Artiste.cherche_nom(x[1], curseur) for x in resultat]
        return None
