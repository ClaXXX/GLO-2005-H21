from src.database import DataBase
from os import getenv
from dotenv import load_dotenv
from src.database.oeuvre import Oeuvre
from src.database.artiste import Artiste
load_dotenv()
db = DataBase()
curseur = db.cursor()


monArtiste = Artiste.cherche_nom('lautre',curseur)

#print(monArtiste.courriel)
#mesArtistes = Artiste.liste_artiste(curseur)


def cherche_nom(nom, curseur=DataBase.cursor()):
    curseur.execute('SELECT * FROM Artiste WHERE nom=%s ;', nom)
    resultat = curseur.fetchone()

    if resultat is not None:
        return {'nom': resultat[1], 'courriel': resultat[0]}
    return None
rech = cherche_nom('alblap',curseur)
#print(rech)


def pour_artiste(nom):
    curseur = DataBase.cursor()
    curseur.execute("SELECT * FROM Oeuvre WHERE auteur=%s;", nom)
    resultat = curseur.fetchall()
    if resultat is not None:
        print([(x[0], x[1], x[2], x[3], x[4], x[5]) for x in resultat])
        return [Oeuvre(x[0], x[1], x[2], x[3], x[4], x[5]).toDict() for x in resultat]
print(pour_artiste('alblap'))


nomArti = 'alblap'
def rechercheArti(nomArti, curseur):
    nomArti = '%' + nomArti + '%'
    curseur.execute('SELECT * FROM Oeuvre WHERE auteur LIKE %s AND enExposition=1;', nomArti)
    resultat = curseur.fetchall()
    if resultat is not None:
        return [Oeuvre.cherche_nom(x[0], curseur).toDict() for x in resultat]
    return None

#print(rechercheArti(nomArti, curseur))

name = "Les Gouffres de l'esprit no 10"
def recherche(nom, curseur):
    nom = '%' + nom + '%'
    curseur.execute('SELECT * FROM Oeuvre WHERE nom LIKE %s ;', nom)
    resultat = curseur.fetchall()
    if resultat is not None:
        return [Oeuvre.cherche_nom(x[0], curseur).toDict() for x in resultat]
    return None
#print(recherche(name,curseur))
