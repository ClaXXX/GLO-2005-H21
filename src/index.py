from flask import Flask
from flask_login import LoginManager, login_required
from src.database import DataBase, client
from flask import render_template, request

from src.database.artiste import Artiste
from src.routes import auth
from src.routes.client import devient_artiste


def create_app(name):
    app = Flask(name)
    login_manager = LoginManager()
    login_manager.init_app(app)
    app.secret_key = b'>u"7f4ZkD,Lflicdn%:j*=)fF29Ccy'

    @login_manager.user_loader
    def getUser(courriel):
        artiste = Artiste.trouveAvecCourriel(courriel)
        if artiste is None:
            return client.Client.trouveAvecCourriel(courriel)
        return artiste

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['POST'])
    def login():
        return auth.login(request)

    @app.route('/register', methods=['POST'])
    def register():
        return auth.register(request)

    @app.route('/logout', methods=['POST'])
    @login_required
    def logout():
        auth.logout()
        return {}

    @app.route('/artiste/devenir', methods=['POST'])
    @login_required
    def devenir_artiste():
        return devient_artiste(request)

    @app.route("/accueil", methods=['GET'])
    def accueil():
        return accueil.expo(DataBase.cursor())

    @app.route("/accueil/oeuvre", methods=['POST'])
    def voir_type():
        return accueil.select_oeuvres(request, DataBase.cursor())

    return app
