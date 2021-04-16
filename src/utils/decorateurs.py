import functools

import flask_login
from flask import abort, request
from pymysql import Error


def retourne_dict(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).getDict()
    return wrapper


def valide_json(*arguments_attendu):
    def decorateur(func):
        @functools.wraps(func)
        def json_wrapper(*args, **kwargs):
            json_objet = request.get_json()
            for expected_arg in arguments_attendu:
                if expected_arg not in json_objet:
                    abort(400)
            return func(*args, **kwargs)
        return json_wrapper
    return decorateur


def doit_etre_artiste(func):
    def artiste_wrapper(*args, **kwargs):
        if not flask_login.current_user.estArtiste():
            abort(401, {'message': 'Vous devez être artiste pour pouvoir créer une oeuvre'})
        return func(*args, **kwargs)
    artiste_wrapper.__name__ = func.__name__
    return artiste_wrapper


def sql_gestion_erreur(func):
    def sql_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Error as err:
            abort(400, {'message': err.args[1]})
    return sql_wrapper