import flask_login
from flask import request

from src.database.artiste import Artiste
from src.database.commande import Commande
from src.database.commentaire import Commentaire
from src.database.oeuvre import Oeuvre


def creer_commande():
    artiste = Artiste.cherche_nom('artiste')
    if artiste is None:
        return {"message": "L'artiste demandé n'existe pas"}, 400
    num_commande = Commande.commander_reservation(request.json.get('artiste'),
                                                  flask_login.current_user.courriel,
                                                  request.json.get('prix'),
                                                  request.json.get('adresseLivraison'))
    Commentaire.ajoute(flask_login.current_user.courriel,
                       num_commande, request.json.get('texte'))
    return {"commande": num_commande}, 201


def reserver_commande():
    artiste = Artiste.cherche_nom('artiste')
    if artiste is None:
        return {"message": "L'artiste demandé n'existe pas"}
    oeuvre = Oeuvre.retrouve_oeuvre(request.json.get('oeuvre'), request.json.get('artiste'))
    if oeuvre is None:
        return {"message": "L'oeuvre demandée n'existe pas"}, 400
    num_commande = Commande.commander_creation(request.json.get('oeuvre'),
                                               request.json.get('artiste'),
                                               flask_login.current_user.courriel,
                                               request.json.get('prix'),
                                               request.json.get('adresseLivraison'))
    Commentaire.ajoute(flask_login.current_user.courriel,
                       num_commande, request.json.get('texte'))
    return {"commande": num_commande}, 201
