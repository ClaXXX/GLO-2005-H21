class Oeuvre:
    def __init__(self, nom, auteur,dateCreation,type,desc,enExpo):
        self.nom = nom
        self.auteur = auteur
        self.dateCreation = dateCreation
        self.type = type
        self.desc = desc
        self.enExpo = enExpo

    def cherche_nom(nom,curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return Oeuvre(resultat[0],resultat[1],resultat[2],resultat[3], resultat[4], resultat[5])
        return None

    def tri_oeuvre(type,curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE type=%s ;',type)
        resultat = curseur.fetchall()

        if resultat is not None:
            liste_oeuvre = [Oeuvre.cherche_nom(x[0],curseur) for x in resultat]
            return liste_oeuvre
        return None

    def oeuvre_parArtiste(auteur,curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE auteur=%s ;', auteur)
        resultat = curseur.fetchall()

        if resultat is not None:
            oeuvres = [Oeuvre.cherche_nom(x[0], curseur) for x in resultat]
            return oeuvres
        return None

    def exposition_totale(curseur):
        curseur.execute('SELECT * FROM Oeuvre WHERE enExposition ORDER BY type;')
        resultat = curseur.fetchall()

        if resultat is not None:
            galerie = [Oeuvre.cherche_nom(x[0],curseur) for x in resultat]
            return galerie
        return None

    def imprime(liste):
        str = ""
        print(liste)
        for x in liste:
            str += x.nom + " par " + x.auteur + " " + "\n"

        return str

