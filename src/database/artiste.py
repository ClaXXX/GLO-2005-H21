import copy

from src.database import DataBase
from src.database.client import Client
from src.database.oeuvre import Oeuvre
from src.utils.decorateurs import sql_gestion_erreur


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

    def toDict(self):
        return {'courriel': self.courriel,'nom': self.nom}

    @staticmethod
    @sql_gestion_erreur
    def trouveAvecCourriel(courriel, curseur=DataBase.cursor()):
        curseur.execute('SELECT * FROM Artiste WHERE courriel=%s ;',courriel)
        artiste = curseur.fetchone()
        if artiste is not None:
            return Artiste(Client.trouveAvecCourriel(courriel=courriel), artiste[1])
        return None

    @staticmethod
    @sql_gestion_erreur
    def devient_artiste(courriel, nom):
        client = Client.trouveAvecCourriel(courriel=courriel)
        if client is None:
            return None
        cursor = DataBase.cursor()
        cursor.execute('INSERT INTO Artiste VALUE (%s, %s);',(courriel,nom))
        return Artiste(client, nom)

    @staticmethod
    @sql_gestion_erreur
    def fin_carriere(courriel):
        cursor = DataBase.cursor()
        cursor.execute('DELETE FROM Artiste WHERE courriel=%s;',courriel)
        return {}


    @staticmethod
    @sql_gestion_erreur
    def cherche_nom(nom, curseur=DataBase.cursor()):
        curseur.execute('SELECT * FROM Artiste WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return {'nom': resultat[1], 'courriel': resultat[0]}
        return None

    @staticmethod
    @sql_gestion_erreur
    def liste_artiste():
        curseur = DataBase.cursor()
        curseur.execute('SELECT * FROM Artiste;')
        resultat = curseur.fetchall()

        if resultat is not None:
            artistes = [Artiste.cherche_nom(x[1], curseur) for x in resultat]
            return artistes
        return None

    @staticmethod
    @sql_gestion_erreur
    def recherche(nom, curseur):
        nom = '%' + nom + '%'
        curseur.execute('SELECT * FROM Artiste WHERE nom  LIKE %s ;', nom)
        resultat = curseur.fetchall()
        if resultat is not None:
            return [Artiste.cherche_nom(x[0],x[1]).toDict() for x in resultat]
        return None
