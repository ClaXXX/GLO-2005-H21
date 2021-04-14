import flask_login

from src.database.artiste import Artiste
from src.utils.decorateurs import retourne_dict


@retourne_dict
def devient_artiste(request):
    return Artiste.devient_artiste(courriel=flask_login.current_user.courriel,
                                      nom=request.json.get('nom'))


def expo(curseur):
    return Artiste.liste_artiste()


def select_artiste(request, curseur):
    nom = request.args.get('nom')

    return Artiste.cherche_nom(nom, curseur)

def recherche(request,curseur):
    return Artiste.recherche(request,curseur)