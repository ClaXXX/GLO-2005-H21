import flask_login
from flask import request

from src.database.oeuvre import Oeuvre


def ajoute_oeuvre():
    en_exposition = request.json.get('enExposition')
    if en_exposition is None or en_exposition == "False":
        en_exposition = False
    else:
        en_exposition = True
    return Oeuvre.ajoute(nom=request.json.get('nom'), auteur=flask_login.current_user.nomArtiste,
                         dateCreation=request.json.get('dateCreation'), type=request.json.get('type'),
                         description=request.json.get('description'), enExposition=en_exposition)


def expo(curseur):
    return Oeuvre.exposition_totale(curseur)


def select_oeuvres(request, curseur):
    type = request.args.get('type')

    return Oeuvre.tri_oeuvre(type, curseur)


def recherche_nom(request, curseur):
    return Oeuvre.par_nom(request, curseur)


def recherche_arti(request, curseur):
    return Oeuvre.par_artiste(request, curseur)


def recherche_type(request, curseur):
    return Oeuvre.par_type(request, curseur)
