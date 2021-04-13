from src.database.artiste import Artiste


def expo(curseur):
    return Artiste.liste_artiste(curseur)


def select_artiste(request, curseur):
    nom = request.args.get('nom')

    return Artiste.cherche_nom(nom, curseur)

def recherche(request,curseur):
    return Artiste.recherche(request,curseur)