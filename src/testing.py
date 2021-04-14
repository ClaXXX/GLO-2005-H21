from src.database import DataBase
from os import getenv
from dotenv import load_dotenv
from src.database.oeuvre import Oeuvre
from src.database.artiste import Artiste
load_dotenv()
db = DataBase(getenv('SQL_HOST'), getenv('SQL_USER'), getenv('SQL_PASSWORD'), getenv('SQL_DB'))
curseur = db.cursor()

monOeuvre = Oeuvre.cherche_nom('La famille',curseur)
#print(monOeuvre)
#print(monOeuvre.dateCreation)

peintures = Oeuvre.tri_oeuvre('Peinture huile',curseur)
galerie = Oeuvre.exposition_totale(curseur)
#print(galerie)

oeuvres = Oeuvre.oeuvre_parArtiste('lautre',curseur)
#print(oeuvres)



monArtiste = Artiste.cherche_nom('lautre',curseur)

#print(monArtiste.courriel)
#mesArtistes = Artiste.liste_artiste(curseur)


def recherche(nom, curseur):
    curseur.execute('SELECT * FROM Artiste WHERE nom =%s ;', nom)
    resultat = curseur.fetchone()
    if resultat is not None:
        return Artiste(resultat[0], resultat[1]).toDict()
    return None

rech = recherche('lautre',curseur)
#print(rech)


nomArti = 'alblap'
def rechercheArti(nomArti, curseur):
    nomArti = '%' + nomArti + '%'
    curseur.execute('SELECT * FROM Oeuvre WHERE auteur LIKE %s AND enExposition=1;', nomArti)
    resultat = curseur.fetchall()
    if resultat is not None:
        return [Oeuvre.cherche_nom(x[0], curseur).toDict() for x in resultat]
    return None

print(rechercheArti(nomArti, curseur))

name = "Les Gouffres de l'esprit no 10"
def recherche(nom, curseur):
    nom = '%' + nom + '%'
    curseur.execute('SELECT * FROM Oeuvre WHERE nom LIKE %s ;', nom)
    resultat = curseur.fetchall()
    if resultat is not None:
        return [Oeuvre.cherche_nom(x[0], curseur).toDict() for x in resultat]
    return None
print(recherche(name,curseur))
