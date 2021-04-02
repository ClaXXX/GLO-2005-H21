class Artiste:
    def __init__(self, courriel, nom):
        self.courriel = courriel
        self.nom = nom

    def cherche_nom(nom,curseur):
        curseur.execute('SELECT * FROM Artiste WHERE nom=%s ;', nom)
        resultat = curseur.fetchone()

        if resultat is not None:
            return Artiste(resultat[0], resultat[1])
        return None

    def liste_artiste(curseur):
        curseur.execute('SELECT * FROM Artiste;')
        resultat = curseur.fetchall()

        if resultat is not None:
            artistes = [Artiste.cherche_nom(x[1], curseur) for x in resultat]
            return artistes
        return None


    def imprime(liste):
        str = ""
        print(liste)
        for x in liste:
            str += x.nom + " " + x.courriel + " " + "\n"

        return str
