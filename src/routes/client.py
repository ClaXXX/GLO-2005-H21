import flask_login

from src.database.artiste import Artiste


def devient_artiste(request):
    courriel = "'" + flask_login.current_user.courriel + "'"
    nom = request.json.get('nom')
    if courriel is None or nom is None:
        return {}, 400
    artiste = Artiste.devient_artiste(courriel, nom).getDict()
    return artiste, 201
