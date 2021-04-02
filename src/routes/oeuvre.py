from src.database.oeuvre import Oeuvre
from flask import render_template

def expo(curseur):
     galerie = Oeuvre.exposition_totale(curseur)

     return render_template('index.html', galerie ={
          'Oeuvres': [x[0].nom for x in galerie]

     })

def select_oeuvres(request, curseur):
     type = request.form.get('type')
     galerie = Oeuvre.tri_oeuvre(type,curseur)

     return render_template('index.html', galerie = {
          'Oeuvres':
     })