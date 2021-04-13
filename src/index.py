from flask import Flask
from src.database import DataBase
from os import getenv, execv
from flask import render_template, request, jsonify
from src.routes import auth
from src.routes import oeuvre
from src.routes import artiste
from dotenv import load_dotenv
from os.path import join, dirname
import json

def create_app(name):
    app = Flask(name)
    app.secret_key = b'>u"7f4ZkD,Lflicdn%:j*=)fF29Ccy'
    load_dotenv()
    database = DataBase(getenv('SQL_HOST'), getenv('SQL_USER'), getenv('SQL_PASSWORD'), getenv('SQL_DB'))

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/login", methods=['POST'])
    def login():
        return auth.login(request, database.cursor())

    @app.route("/oeuvre", methods=['GET'])
    def recup_oeuvre():
        response = {
            "status": 200,
            "oeuvre": oeuvre.expo(database.cursor())
        }
        return jsonify(response)

    @app.route("/artiste", methods=['GET'])
    def recup_artiste():
        response = {
            "status": 200,
            "artiste": artiste.expo(database.cursor())
        }
        return jsonify(response)


    @app.route("/search/", methods=['GET'])
    def recherche():
        type = request.args.get('type')
        recherche = request.args.get('recherche')
        if type == 'Artiste':
            response = {
                "status": 200,
                "oeuvre": oeuvre.recherche_arti(recherche, database.cursor())
            }
            return jsonify(response)
        elif type == 'Oeuvre':
            response = {
                "status": 200,
                "oeuvre": oeuvre.recherche_nom(recherche, database.cursor())
            }
            return jsonify(response)
        elif type == 'Type':
            response = {
                "status": 200,
                "oeuvre": oeuvre.recherche_type(recherche, database.cursor())
            }
            return jsonify(response)
    return app
