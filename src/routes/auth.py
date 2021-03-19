from flask import render_template, session
from ..database.auth import Auth


def login(request, cursor):
    user = Auth('"' + request.form.get('courriel') + '"',
                request.form.get('motpasse'))
    client = user.login(cursor)
    if client is not None:
        # session[client.courriel] = client
        return render_template('index.html', profile={
            'courriel': client.courriel,
            'nom': client.nom,
            'avatar': client.avatar
        })
    return render_template('login.html', message="Informations invalides!")
