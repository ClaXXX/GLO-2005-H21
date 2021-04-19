from datetime import datetime
import json
import time

from src.database import DataBase
from src.utils.decorateurs import sql_gestion_erreur


class Oeuvre:
    def __init__(self, nom, auteur, dateCreation, type, desc, enExpo):
        self.nom = nom
        self.auteur = auteur
        if dateCreation is None:
            self.dateCreation = 'Non définie'
        else:
            self.dateCreation = dateCreation.strftime("%Y-%b-%d")
        if type is None:
            self.type = 'Type non défini'
        else:
            self.type = type
        if desc is None:
            self.desc = 'Aucune description'
        else:
            self.desc = desc
        if enExpo is None:
            self.enExpo = 0
        else:
            self.enExpo = enExpo

    def toDict(self):
        return {'nom': self.nom, 'auteur': self.auteur,'dateCreation':self.dateCreation,'type':self.type,'desc':self.desc, 'enExposition':self.enExpo}

    @staticmethod
    @sql_gestion_erreur
    def ajoute(nom, auteur, dateCreation, type='', description='', enExposition=False, cursor = DataBase.cursor()):
        cursor.execute("INSERT INTO Oeuvre (nom, auteur, dateCreation, type, description, enExposition) VALUE"
                       " (%s, %s,STR_TO_DATE(%s,'%Y-%m-%d'),%s,%s,%s);",
                       (nom, auteur, dateCreation, type, description, enExposition))
        return {}

    @staticmethod
    @sql_gestion_erreur
    def retrouve_oeuvre(nom, artiste, curseur=DataBase.cursor()):
        curseur.execute("SELECT * FROM Oeuvre WHERE nom=%s AND auteur=%s;", (nom, artiste))
        oeuvre = curseur.fetchone()
        return Oeuvre(oeuvre[0], oeuvre[1], oeuvre[2], oeuvre[3], oeuvre[4], oeuvre[5]).toDict()

    @staticmethod
    @sql_gestion_erreur
    def supprime(nom, auteur):
        cursor = DataBase.cursor()
        cursor.execute('DELETE FROM Oeuvre WHERE nom = %s AND auteur = %s',(nom,auteur))
        return {}

    @staticmethod
    @sql_gestion_erreur
    def pour_artiste(nom):
        curseur = DataBase.cursor()
        curseur.execute("SELECT * FROM Oeuvre WHERE auteur=%s;", nom)
        resultat = curseur.fetchall()
        if resultat is not None:
            return [Oeuvre(x[0], x[1], x[2], x[3], x[4], x[5]).toDict() for x in resultat]

    @staticmethod
    @sql_gestion_erreur
    def cherche_db(nom, curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return Oeuvre(resultat[0],resultat[1],resultat[2],resultat[3], resultat[4], resultat[5])
        return None

    @staticmethod
    @sql_gestion_erreur
    def par_type(type,curseur):
        type = '%' + type + '%'
        curseur.execute('SELECT * FROM Oeuvre WHERE type LIKE %s AND enExposition=1 ;',type)
        resultat = curseur.fetchall()

        if resultat is not None:
            liste_oeuvre = [Oeuvre(x[0],x[1],x[2],x[3],x[4],x[5]).toDict() for x in resultat]
            return liste_oeuvre
        return None

    @staticmethod
    @sql_gestion_erreur
    def par_artiste(auteur,curseur):
        auteur = '%' + auteur + '%'
        curseur.execute('SELECT * FROM Oeuvre WHERE auteur LIKE %s AND enExposition=1 ;', auteur)
        resultat = curseur.fetchall()

        if resultat is not None:
            oeuvres = [Oeuvre(x[0],x[1],x[2],x[3],x[4],x[5]).toDict() for x in resultat]
            return oeuvres
        return None

    @staticmethod
    @sql_gestion_erreur
    def exposition_totale(curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE enExposition GROUP BY type;')
        resultat = curseur.fetchall()
        print(resultat)
        if resultat is not None:
            galerie = [Oeuvre(x[0],x[1],x[2],x[3],x[4],x[5]).toDict() for x in resultat]
            return galerie
        return None

    @staticmethod
    @sql_gestion_erreur
    def par_nom(nom, curseur):
        nom = '%' + nom + '%'
        curseur.execute('SELECT * FROM Oeuvre WHERE nom LIKE %s AND enExposition=1;', nom)
        resultat = curseur.fetchall()
        if resultat is not None:
            return [Oeuvre(x[0],x[1],x[2],x[3],x[4],x[5]).toDict() for x in resultat]
        return None

