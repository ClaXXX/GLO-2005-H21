class Artiste:
    def __init__(self, courriel, nom):
        self.courriel = courriel
        self.nom = nom

    def toDict(self):
        return {'courriel': self.courriel,'nom': self.nom}

    @staticmethod
    def cherche_nom(nom,curseur):
        curseur.execute('SELECT * FROM Artiste WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return Artiste(resultat[0], resultat[1])
        return None

    @staticmethod
    def liste_artiste(curseur):
        curseur.execute('SELECT * FROM Artiste;')
        resultat = curseur.fetchall()

        if resultat is not None:
            artistes = [Artiste.cherche_nom(x[1], curseur).toDict() for x in resultat]
            return artistes
        return None

    @staticmethod
    def recherche(nom, curseur):
        nom = '%' + nom + '%'
        curseur.execute('SELECT * FROM Artiste WHERE nom  LIKE %s ;', nom)
        resultat = curseur.fetchall()
        if resultat is not None:
            return [Artiste.cherche_nom(x[1], curseur).toDict() for x in resultat]
        return None
