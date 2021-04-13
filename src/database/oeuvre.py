import json
class Oeuvre:
    def __init__(self, nom, auteur, dateCreation, type, desc, enExpo):
        self.nom = nom
        self.auteur = auteur
        self.dateCreation = dateCreation.strftime("%Y-%b-%d")

        self.type = type
        self.desc = desc
        self.enExpo = enExpo

    def toDict(self):
        return {'nom': self.nom, 'auteur': self.auteur,'dateCreation':self.dateCreation,'type':self.type,'desc':self.desc, 'enExposition':self.enExpo}


    @staticmethod
    def cherche_db(nom, curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return Oeuvre(resultat[0],resultat[1],resultat[2],resultat[3], resultat[4], resultat[5])
        return None

    @staticmethod
    def par_type(type,curseur):
        type = '%' + type + '%'
        curseur.execute('SELECT * FROM Oeuvre WHERE type LIKE %s AND enExposition=1 ;',type)
        resultat = curseur.fetchall()

        if resultat is not None:
            liste_oeuvre = [Oeuvre.cherche_db(x[0],curseur).toDict() for x in resultat]
            return liste_oeuvre
        return None

    @staticmethod
    def par_artiste(auteur,curseur):
        auteur = '%' + auteur + '%'
        curseur.execute('SELECT * FROM Oeuvre WHERE auteur LIKE %s AND enExposition=1 ;', auteur)
        resultat = curseur.fetchall()

        if resultat is not None:
            oeuvres = [Oeuvre.cherche_db(x[0], curseur).toDict() for x in resultat]
            return oeuvres
        return None

    @staticmethod
    def exposition_totale(curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE enExposition ORDER BY type;')
        resultat = curseur.fetchall()

        if resultat is not None:
            galerie = [Oeuvre.cherche_db(x[0],curseur).toDict() for x in resultat]
            return galerie
        return None

    @staticmethod
    def par_nom(nom, curseur):
        nom = '%' + nom + '%'
        curseur.execute('SELECT * FROM Oeuvre WHERE nom LIKE %s AND enExposition=1;', nom)
        resultat = curseur.fetchall()
        if resultat is not None:
            return [Oeuvre.cherche_db(x[0], curseur).toDict() for x in resultat]
        return None

