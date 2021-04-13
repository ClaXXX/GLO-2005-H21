from flask_login import login_user, logout_user
from flask import abort, flash

from ..database.artiste import Artiste
from ..database.client import Client


def login(request):
    if request.json is None:
        abort(400)
    courriel = "'" + request.json.get('courriel') + "'"
    mdp = request.json.get('mdp')
    if courriel is None or mdp is None:
        return abort(400)
    user = Client.login(courriel, mdp)
    if user is not None:
        artiste = Artiste.trouveAvecCourriel(courriel)
        if artiste is not None:
            login_user(artiste)
        else:
            login_user(user)

        flash('Logged in successfully.')

        return {}, 200
    return {'message': "Informations invalides!"}, 400


def register(request):
    courriel = "'" + request.json.get('courriel') + "'"
    mdp = "'" + request.json.get('mdp') + "'"
    nom = "'" + request.json.get('nom') + "'"
    prenom = "'" + request.json.get('prenom') + "'"
    adresse = "'" + request.json.get('adresse') + "'"
    if courriel is None or mdp is None:
        return abort(400)
    user = Client.register(courriel=courriel, mdp=mdp, nom=nom, prenom=prenom, adresse=adresse)
    login_user(user)
    return user.getDict(), 201


def logout():
    logout_user()
