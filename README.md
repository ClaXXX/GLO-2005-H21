# GLO-2005-H21
## Description
Tp de programmation dans le cadre du cours GLO-2005. Le sujet de ce projet sera de créer une boutique en ligne spécialisée dans la vente d’objets d’art. Elle permet aux artistes de vendre leurs œuvres et de prendre des commandes.

## Prérequis
- [Python](https://www.python.org/) 3.+ minimum
- [Poetry](https://python-poetry.org/docs/)

## Installation
Poetry est un outil qui permet de gérer les dépendances et packets d'un projet avec Python. Il sera notamment utils pour sa gestion d'environnement virtuel.
```shell
poetry install
```

## Configuration
Le package Dotenv permet de déclarer l'ensemble des variables d'environnement dans un fichier .env. Ainsi pour ce projet, nous aurons un modèle de fichier:
```dotenv
FLASK_APP=src/main.py
SQL_HOST=localhost
SQL_USER=root
SQL_PASSWORD=password
SQL_DB=artshale
```

## Execution
### Environnement virtuel
Pour pouvoir faire tourner l'ensemble de l'application en installant toutes les dépendances localement dans le fichier, il est interressant de pouvoir faire tourner l'application dans un environnement virtuel. De plus, cela permet d'éviter des soucis de versions entre les dépendances.
Les commandes les plus importantes sont:
```shell
poetry shell # permet de démarrer l'éxecuteur de commande pour notre environnement virtuel
exit # Sort de l'environnement virtuel (fonctionne aussi via Ctrl+d)
```

### Flask
```shell
flask run
```