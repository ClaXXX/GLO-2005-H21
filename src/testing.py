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
print(galerie)

oeuvres = Oeuvre.oeuvre_parArtiste('lautre',curseur)
#print(oeuvres)


print(Oeuvre.imprime(galerie))

monArtiste = Artiste.cherche_nom('lautre',curseur)
print(monArtiste.courriel)
mesArtistes = Artiste.liste_artiste()

print(Artiste.imprime(mesArtistes))

