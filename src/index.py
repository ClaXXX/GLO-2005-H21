import flask_login
from flask import Flask

from flask_login import LoginManager, login_required, logout_user
from src.database import DataBase, client
from flask import render_template, request, jsonify

from src.database.artiste import Artiste
from src.database.client import Client
from src.database.commande import Commande
from src.database.commentaire import Commentaire
from src.database.oeuvre import Oeuvre
from src.database.facture import Facture
from src.routes import auth, commande
from src.routes import oeuvre, artiste, facture
from src.routes.artiste import devient_artiste
from src.utils.decorateurs import valide_json, doit_etre_artiste


def create_app(name):
    app = Flask(name)
    login_manager = LoginManager()
    login_manager.init_app(app)
    app.secret_key = b'>u"7f4ZkD,Lflicdn%:j*=)fF29Ccy'

    # Fonction demandee pour flask-login
    @login_manager.user_loader
    def getUser(courriel):
        artiste = Artiste.trouveAvecCourriel(courriel=courriel)
        if artiste is not None:
            return artiste
        return Client.trouveAvecCourriel(courriel=courriel)

    # pages
    @app.route("/")
    def index():
        return render_template('index.html', titre="Home", fichier='home.html')

    @app.route("/artiste/<nom>")
    def profile(nom):
        artiste = Artiste.cherche_nom(nom)
        return render_template('index.html', titre=nom,
                               fichier='artiste/profil.html',
                               artiste=artiste,
                               oeuvres=Oeuvre.pour_artiste(nom))

    @app.route("/factures")
    @doit_etre_artiste
    def factures():
        return render_template('index.html', titre="Mes factures", fichier="Facture/factures.html", factures=facture.sommaire_artiste())

    @app.route("/commandes")
    @login_required
    def mes_commandes():
        return render_template('index.html', titre='Mes commandes',
                               fichier='commande/commandes.html',
                               commandes=Commande.mes_commandes(flask_login.current_user.courriel))

    # authentification
    @app.route('/connection', methods=['POST'])
    @valide_json("courriel", "mdp")
    def connection():
        return auth.connection(), 200

    @app.route('/creer_compte', methods=['POST'])
    @valide_json("courriel", "mdp", "nom", "prenom", "adresse")
    def nouveau_compte():
        return auth.creer_compte(), 201

    @app.route('/deconnection', methods=['PUT'])
    @login_required
    def deconnection():
        logout_user()
        return {}, 200

    # artiste
    @app.route('/artiste/devenir', methods=['POST'])
    @valide_json('nom')
    @login_required
    def devenir_artiste():
        return devient_artiste(request), 201

    @app.route('/artiste/finir', methods=['DELETE'])
    @doit_etre_artiste
    def finir_artiste():
        return artiste.fin_artiste(), 200

    @app.route("/artiste", methods=['GET'])
    def recup_artiste():
        response = {
            "status": 200,
            "artiste": artiste.expo(DataBase.cursor())
        }
        return jsonify(response)

    # oeuvre
    @app.route("/oeuvre", methods=['GET'])
    def recup_oeuvre():
        response = {
            "status": 200,
            "oeuvre": oeuvre.expo(DataBase.cursor())
        }
        return jsonify(response)

    @app.route("/oeuvre/creer", methods=['POST'])
    @valide_json('nom', 'dateCreation', 'type', 'description')
    @doit_etre_artiste
    def creer_oeuvre():
        return oeuvre.ajoute_oeuvre(), 201

    @app.route("/oeuvre/supprimer", methods=['DELETE'])
    @valide_json('nom', 'auteur')
    @doit_etre_artiste
    def supprimer_oeuvre():
        return oeuvre.supprime_oeuvre(), 200

    @app.route("/search/", methods=['GET'])
    def recherche():
        type = request.args.get('type')
        recherche = request.args.get('recherche')
        if type == 'Artiste':
            response = {
                "status": 200,
                "oeuvre": oeuvre.recherche_arti(recherche, DataBase.cursor())
            }
            return jsonify(response)
        elif type == 'Oeuvre':
            response = {
                "status": 200,
                "oeuvre": oeuvre.recherche_nom(recherche, DataBase.cursor())
            }
            return jsonify(response)
        elif type == 'Type':
            response = {
                "status": 200,
                "oeuvre": oeuvre.recherche_type(recherche, DataBase.cursor())
            }
            return jsonify(response)

    # Commandes
    @app.route("/commande", methods=['GET'])
    @login_required
    def retourne_commandes():
        return {"commandes": Commande.mes_commandes(flask_login.current_user.courriel)}, 200

    @app.route("/commande/artiste", methods=['GET'])
    @doit_etre_artiste
    def commande_artiste():
        return {"commandes": Commande.commande_artiste(flask_login.current_user.nomArtiste)}, 200

    @app.route("/commande/creer", methods=['POST'])
    @login_required
    @valide_json('oeuvre', 'artiste', 'prix', 'adresseLivraison', 'commentaire')
    def creer_commande():
        return commande.creer_commande()

    @app.route("/commande/reserver", methods=['POST'])
    @login_required
    @valide_json('artiste', 'prix', 'adresseLivraison', 'commentaire')
    def reserver_commande():
        return commande.reserver_commande()

    @app.route("/commande/<numCommande>/commentaires", methods=['GET'])
    @login_required
    def recupere_commentaires(numCommande):
        return {'commentaires': Commentaire.recupere_tous(numCommande=numCommande)}, 200

    @app.route("/commande/<numCommande>/ajouteCommentaire", methods=['POST'])
    @login_required
    @valide_json('texte')
    def ajoute_commentaire(numCommande):
        Commentaire.ajoute(flask_login.current_user.courriel,
                           numCommande, request.json.get('texte'))
        return {}, 201

    # Factures
    @app.route("/commande/<numCommande>/facture", methods=['GET'])
    @login_required
    def recupere_factures(numCommande):
        return {'factures': Facture.recup_fac(numCommande=numCommande)}, 200

    @app.route("/commande/<numCommande>/facturation", methods=['POST'])
    @login_required
    @valide_json('numCommande', 'adresseFac', 'total')
    def facturer(numCommande):
        return facture.facturer(request), 201


    return app
