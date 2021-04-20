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
        return {'num': self.num, 'oeuvre': self.oeuvre, 'superviseur': self.superviseur, 'demandeur': self.demandeur,
                'statut': self.statut, 'prix': self.prix, 'type': self.type}

    @staticmethod
    @sql_gestion_erreur
    def mes_commandes(courriel, curseur=DataBase.cursor()):
        curseur.execute("SELECT * FROM Commande WHERE demandeur=%s", courriel)
        commandes = curseur.fetchall()
        if commandes is not None:
            return [Commande(c[0], c[1], c[2], c[3], c[4], c[5], c[6]).toDict() for c in commandes]

    @staticmethod
    @sql_gestion_erreur
    def commande_artiste(nom, curseur=DataBase.cursor()):
        curseur.execute("SELECT * FROM Commande WHERE superviseur=%s", nom)
        commandes = curseur.fetchall()
        if commandes is not None:
            return [Commande(c[0], c[1], c[2], c[3], c[4], c[5], c[6]).toDict() for c in commandes]

    @staticmethod
    @sql_gestion_erreur
    def commander_reservation(oeuvre, superviseur, demandeur, prix, adresse_livraison, curseur=DataBase.cursor()):
        print("Reserve commande")
        curseur.execute("INSERT INTO Commande (oeuvre, superviseur, demandeur, prix, type) VALUE (%s, %s, %s, %s, %s)", (oeuvre, superviseur, demandeur, prix, adresse_livraison))
        curseur.execute("SELECT MAX(num) FROM Commande;")
        num = curseur.fetchone()
        print(num)
        return num  # retourne le numero de la commande créée

    @staticmethod
    @sql_gestion_erreur
    def commander_creation(superviseur, demandeur, prix, adresse_livraison, curseur=DataBase.cursor()):
        curseur.execute("INSERT INTO Commande (superviseur, demandeur, prix, type) VALUE (%s, %s, %s, %s)", (superviseur, demandeur, prix, adresse_livraison))
        curseur.execute("SELECT MAX(num) FROM Commande;")
        return curseur.fetchone()  # retourne le numero de la commande créée
