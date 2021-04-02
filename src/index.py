from flask import Flask
from src.database import DataBase
from os import getenv, execv
from flask import render_template, request
from src.routes import auth
from src.routes import accueil
from dotenv import load_dotenv
from os.path import join, dirname

def create_app(name):
    app = Flask(name)
    app.secret_key = b'>u"7f4ZkD,Lflicdn%:j*=)fF29Ccy'
    load_dotenv()
    database = DataBase(getenv('SQL_HOST'), getenv('SQL_USER'), getenv('SQL_PASSWORD'), getenv('SQL_DB'))

    @app.route("/")
    def index():
        return render_template('login.html')

    @app.route("/login", methods=['POST'])
    def login():
        return auth.login(request, database.cursor())
    @app.route("/accueil", methods=['GET'])
    def accueil():
        return accueil.expo(database.cursor())

    @app.route("/accueil/oeuvre", methods=['POST'])
    def voir_type():
        return accueil.select_oeuvres(request, database.cursor)

    return app
