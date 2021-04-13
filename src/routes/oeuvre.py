from src.database.oeuvre import Oeuvre


def expo(curseur):
     return Oeuvre.exposition_totale(curseur)

def select_oeuvres(request, curseur):
     type = request.args.get('type')

     return Oeuvre.tri_oeuvre(type,curseur)

def recherche_nom(request,curseur):
    return Oeuvre.par_nom(request,curseur)

def recherche_arti(request,curseur):
    return Oeuvre.par_artiste(request,curseur)
def recherche_type(request,curseur):
    return Oeuvre.par_type(request,curseur)