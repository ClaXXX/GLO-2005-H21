from src.database import DataBase
from src.utils.decorateurs import *


class Commentaire:
    def __init__(self, id, auteur, numCommande, texte, creation):
        self.id = id
        self.auteur = auteur
        self.numCommande = numCommande
        self.texte = texte
        self.creation = creation

    def getDict(self):
        return {'id': self.id, 'auteur': self.auteur, 'commande': self.numCommande,
                'texte': self.texte, 'creation': self.creation}

    @staticmethod
    @sql_gestion_erreur
    def ajoute(auteur, numCommande, texte, curseur=DataBase.cursor()):
        curseur.execute("INSERT INTO Commentaire (auteur, numCommande, texte) VALUE (%s)",
                        f"{auteur}, {numCommande}, {texte}")
        return {}  # TODO: <- retravailler le retour fonction

    @staticmethod
    @sql_gestion_erreur
    def recupere_tous(numCommande, curseur=DataBase.cursor()):
        curseur.execute("SELECT * FROM Commentaire WHERE numCommande=%s", numCommande)
        return [Commentaire(c[0], c[1], c[2], c[3], c[4]).getDict() for c in curseur.fetchall()]
