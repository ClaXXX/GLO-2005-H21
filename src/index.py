from flask import Flask
from src.database import DataBase
from os import getenv, execv
from flask import render_template, request
from src.routes import auth


def create_app(name):
    app = Flask(name)
    app.secret_key = b'>u"7f4ZkD,Lflicdn%:j*=)fF29Ccy'
    database = DataBase(getenv('SQL_HOST'), getenv('SQL_USER'), getenv('SQL_PASSWORD'), getenv('SQL_DB'))

    @app.route("/")
    def index():
        return render_template('login.html')

    @app.route("/login", methods=['POST'])
    def login():
        return auth.login(request, database.cursor())

    return app
