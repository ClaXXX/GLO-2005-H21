from flask_login import login_user
from flask import abort, flash, request

from ..database.artiste import Artiste
from ..database.client import Client
from ..utils.decorateurs import retourne_dict


@retourne_dict
def connection():
    user = Client.connection(courriel=request.json.get('courriel'),
                             mdp=request.json.get('mdp'))
    print(user)
    if user is None:
        abort(400, {'message': "Informations invalides!"})
    artiste = Artiste.trouveAvecCourriel(courriel=user.courriel)
    if artiste is not None:
        print(artiste)
        login_user(artiste)
        flash('Connection réussie. Connecté en tant que artiste')
    else:
        login_user(user)
        flash('Connection réussie. Connecté en tant que client')
    return user


@retourne_dict
def creer_compte():
    user = Client.creer(courriel=request.json.get('courriel'),
                        mdp=request.json.get('mdp'),
                        nom=request.json.get('nom'),
                        prenom=request.json.get('prenom'),
                        adresse=request.json.get('adresse'))
    flash('Création de compte réussie')
    login_user(user)
    return user
