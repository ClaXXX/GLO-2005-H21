import flask_login
from flask import request

from src.database.artiste import Artiste
from src.database.commande import Commande
from src.database.commentaire import Commentaire
from src.database.oeuvre import Oeuvre


def creer_commande():
    print("Création d'oeuvre appelé")
    num_commande = Commande.commander_creation(request.json.get('artiste'),
                                                  flask_login.current_user.courriel,
                                                  request.json.get('prix'),
                                                  request.json.get('adresseLivraison'))
    Commentaire.ajoute(flask_login.current_user.courriel,
                       num_commande, request.json.get('commentaire'))
    return {"commande": num_commande}, 201


def reserver_commande():
    print("Hello world")
    num_commande = Commande.commander_reservation(request.json.get('oeuvre'),
                                               request.json.get('artiste'),
                                               flask_login.current_user.courriel,
                                               request.json.get('prix'),
                                               request.json.get('adresseLivraison'))
    Commentaire.ajoute(flask_login.current_user.courriel,
                       num_commande, request.json.get('commentaire'))
    return {"commande": num_commande}, 201
