from src.database import DataBase
from src.utils.decorateurs import *

class Facture:
    def __init__(self, numFac, numCmd, adresseFac, total):
        self.numFac = numFac
        self.numCmd = numCmd
        self.adresseFac = adresseFac
        self.total = total

    def getDict(self):
        return {'numFac': self.numFac,'numCmd': self.numCmd, 'adresseFac':self.adresseFac, 'total':self.total}

    @staticmethod
    @sql_gestion_erreur
    def recup_fac(numCmd, curseur =DataBase.cursor()):

        curseur.execute('SELECT * FROM Facture WHERE numCommande=%s',numCmd)
        return [Facture(f[0],f[1],f[2],f[3]).getDict() for f in curseur.fetchall()]

    @staticmethod
    @sql_gestion_erreur
    def listefac(arti, curseur=DataBase.cursor()):
        curseur.execute('SELECT * FROM Facture F, Commande C WHERE F.numCommande=C.num AND C.superviseur =%s', arti)
        return [Facture(f[0], f[1], f[2], f[3]).getDict() for f in curseur.fetchall()]

    @staticmethod
    @sql_gestion_erreur
    def facturer(numCmd,adresseFac,total, curseur=DataBase.cursor()):
        curseur.execute('INSERT INTO Facture VALUES (%s,%s,%s)',(numCmd,adresseFac,total))
