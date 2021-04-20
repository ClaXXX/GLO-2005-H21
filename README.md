# GLO-2005-H21
## Description
Tp de programmation dans le cadre du cours GLO-2005.
Le sujet de ce projet sera de créer une boutique en ligne spécialisée dans la vente d’objets d’art. Elle permet aux artistes de vendre leurs œuvres et de prendre des commandes.

## Architecture du dossier
    .
    ├── db                      # Ensemble des scripts à exécuter dans mysql
    ├── docs                    # Vidéo et rapport de présentation
    ├── src                     # Fichiers python qui corresponds au serveur d'application
    │   └── index.py            # Ficher qui contient toutes les routes du serveur
    ├── statis                  # Scripts javascript
    │   ├── assets              # Images et autres ressources
    │   └── style               # Css
    └── templates               # Ensemble des templates de l'applications (html)

## Outils externes utilisés
### Serveur
Ces librairies sont nécessaires pour pouvoir faire fonctionner le serveur d'application sous la [Python](https://www.python.org/) 3.+ minimum.
- panda
- Unidecode
- python-lorem (pour la génération de la base de données)
- python-dotenv
- Flask-Login
- passlib
### Client
Pour pouvoir gérer au plus simple l'ensemble des formulaires, le framework [Vue.js](https://vuejs.org/) a été inclu dans l'application.
Un thème [bootstrap](https://getbootstrap.com/) aussi a été inclus pour fournir des classes css.

## Configuration
### Environnement
Le package Dotenv permet de déclarer l'ensemble des variables d'environnement dans un fichier .env. Ainsi pour ce projet, nous aurons un modèle de fichier:
```dotenv
FLASK_APP=src/main.py
SQL_HOST=localhost
SQL_USER=root
SQL_PASSWORD=password
SQL_DB=artshale
```
### Base de donnée
Le projet contient deux scripts à faire tourner dans le serveur de base de donnée. Le premier (schemas.sql) défini l'ensemble des relations. Le second (gachettes.sql), lui, définit l'ensemble des gachettes. Ainsi la mise en place de la base de donnée s'effectue via les commandes suivantes:
```shell
mysql -u root -p < db/schemas.sql # Créé toutes les tables
mysql -u root -p < db/gachettes.sql # Créé les gachettes
```
Une fois le squelette de la base de donnée mis en place, il faut pouvoir peupler la base de donnée. Pour cela, il suffit d'executer le script python src/database/peuplementBD.py. L'ensemble des mots de passe non hashé seront affichés dans l'ordre de création des utilisateurs.
```shell
python src/database/peuplementBD.py
```

## Execution
### Flask
```shell
export FLASK_APP=main.py
flask run
```
### Python
```shell
python main.py
```