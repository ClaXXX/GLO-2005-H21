import flask_login
from flask import request

from src.database.facture import Facture

def facturer(request):
    return Facture.facturer(numCmd=request.json.get('numCmd'), adresseFac=request.json.get('adresseFac'),
                            total=request.json.get('total'))

def sommaire_artiste():
    return Facture.listefac(arti=flask_login.current_user.nomArtiste)

