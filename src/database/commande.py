from src.database import DataBase
from src.utils.decorateurs import sql_gestion_erreur


class Commande:
    def __init__(self, num, oeuvre, superviseur, demandeur, statut, prix, commande_type):
        self.num = num
        self.oeuvre = oeuvre
        self.superviseur = superviseur
        self.demandeur = demandeur
        self.statut = statut
        self.prix = prix
        self.type = commande_type

    def toDict(self):
        return { 'num': self.num, 'oeuvre': self.oeuvre, 'superviseur': self.superviseur, 'demandeur': self.demandeur,
                 'statut': self.statut, 'prix': self.prix, 'type': self.type }

    @staticmethod
    @sql_gestion_erreur
    def mes_commandes(courriel):
        curseur = DataBase.cursor()
        curseur.execute("SELECT * FROM Commande WHERE demandeur=%s", courriel)
        commandes = curseur.fetchall()
        if commandes is not None:
            return [Commande(c[0], c[1], c[2], c[3], c[4], c[5], c[6]).toDict() for c in commandes]
