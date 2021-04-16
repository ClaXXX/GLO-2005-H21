import pandas as pd
from src.database import DataBase
from os import getenv
from dotenv import load_dotenv
import unidecode as uni
import random
import string
from dateutil.relativedelta import *
import datetime
import lorem
from passlib.hash import sha256_crypt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

# Connection à la bd pour peupler les tables
load_dotenv()
db = DataBase()
curseur = db.cursor()

def peupler(df, nom_table):
    cols = ",".join([str(i) for i in df.columns.tolist()])  # str des attributs à insérer dans la déclaration SQL
    for i, rang in df.iterrows():
        cmd = "INSERT INTO "+ nom_table+" (" + cols + " ) VALUES (" + "%s," * (len(rang) - 1) + "%s)"
        curseur.execute(cmd, tuple(rang))


"""
Création et peuplement de la table Client
"""
# Création des mot de passes clients
def gen_MP():
    lettres = string.ascii_letters
    chiffres = string.digits
    chars = lettres + chiffres
    mdp = "".join(random.choice(chars) for x in range(random.randint(3,4)))
    print(mdp)
    return mdp

# création d'un dataframe Client via lecture du fichier .csv contenant noms accentués
df = pd.read_csv('nomClient2.csv', encoding='latin1')

#Concaténation de l'adresse
df['adresse'] = df['adresse_rue'] + ', ' + df['ville'] +' '+  df['code_postal']
df.drop(['adresse_rue','ville','code_postal'],axis=1,inplace=True)

# Création des adresses courriels à partir des nom et prénom des clients
df = df.assign(courriel = df['prenom'] + '.' + df['nom'])
df['courriel'] =df['courriel'].apply(lambda x: uni.unidecode(x.lower()) + '@gmail.com') #création du courriel sans accents et en minuscule

#Création de la colonne mdp

#Peuplement de la table Client
peupler(df,'Client')

df_u = df[['courriel']].copy()
df_u = df_u.assign(mdp=[sha256_crypt.hash(gen_MP()) for x in range(len(df_u))])
peupler(df_u,'Utilisateur')


"""
Création et peuplement de la table Artiste
"""
# création du dataframe Artiste
df_a = df[['courriel']].iloc[0:100].copy()
df_a = df_a.assign(nom= df['prenom'].apply(lambda x: x[0:3]) + df['nom'].apply(lambda x: x[0:3])) #nomArtiste : concat des 3 premières lettres du prenom et nom
df_a['nom'] = df_a['nom'].apply(lambda x: x.lower())

#Peuplement de la table
peupler(df_a,'Artiste')


"""
Création et peuplement de la table Oeuvre
"""
def gen_date():
    aujour = datetime.date.today()
    date_creation = aujour + relativedelta(years=-random.randint(0,10), months=-random.randint(0,12), days=  -random.randint(0,31))
    return date_creation

def type_oeuvre():
    types = ['Sculpture','Gravure','Peinture huile', 'Aquarelle', 'Impression', 'Dessin', 'Dessin numérique', 'Livre', 'Poterie', 'Autres']
    return random.choice(types)

def desc_oeuvre():
    phrase = lorem.get_sentence(count=2, comma=(0, 2), word_range=(4, 6))
    return phrase

#Création du dataframe oeuvre
df_oeu = pd.read_csv('nomOeuvre.csv', encoding='latin1')
df_oeu = df_oeu.assign(auteur=df_a['nom'].iloc[:100,].copy())
df_oeu['auteur'].iloc[100:126] = df_a['nom'].iloc[:26,].copy()
df_oeu = df_oeu.assign(dateCreation=[gen_date() for x in range(len(df_oeu))])
df_oeu = df_oeu.assign(type=[type_oeuvre() for x in range(len(df_oeu))])
df_oeu = df_oeu.assign(description=[desc_oeuvre() for x in range(len(df_oeu))])
df_oeu['enExposition']= [1]*len(df_oeu)
df_oeu['enExposition'].iloc[50:126,] = [0]*76

#Peuplement de la table
peupler(df_oeu,'Oeuvre')


"""
Création et peuplement de la table Commande
"""
def prix_cmd():
    prix = random.randint(10,500)
    return prix

#Création du dataframe Commande
df_cmd = pd.DataFrame(columns =['superviseur','oeuvre','demandeur','statut','prix','type','adresseLivraison'], index=range(150))
df_cmd['superviseur'].iloc[:100,] = df_oeu['auteur'].iloc[:100,].copy()
df_cmd['superviseur'].iloc[100:150,] = df_oeu['auteur'].iloc[:50,].copy()
df_cmd['oeuvre'] = df_oeu['nom'].iloc[:126,].copy()
df_cmd['oeuvre'].iloc[126:150,] = ['sans titre' + str(x) for x in range(24)]
df_cmd['demandeur'].iloc[:100,] = df['courriel'].iloc[100:200,].copy()
df_cmd['demandeur'].iloc[100:150,] = df['courriel'].iloc[100:150,].copy()
df_cmd['statut'].iloc[:50,] = ['En attente de confirmation']*50
df_cmd['statut'].iloc[50:126,] = ['Complétée']*76
df_cmd['statut'].iloc[126:150,] = ['En cours']*24
df_cmd['prix'] = [prix_cmd() for x in range(len(df_cmd))]
df_cmd['type'].iloc[:126,] = ['Réservation']*126
df_cmd['type'].iloc[126:150,] = ['Création']*24
df_cmd['adresseLivraison'].iloc[:100] = df['adresse'].iloc[100:200].copy()
df_cmd['adresseLivraison'].iloc[100:150] = df['adresse'].iloc[100:150].copy()


#Peuplement de la table commande
peupler(df_cmd,'Commande')


"""
Création et peuplement de la table Commentaire
"""
def gen_texte():
    texte = lorem.get_sentence(count=1, comma=(0, 2), word_range=(3, 4))
    return texte

#Création du dataframe Commentaire
df_com =  pd.DataFrame(columns =['auteur','numCommande','texte'], index=range(100))
df_com['auteur'].iloc[:50,] = df['courriel'].iloc[:50,].copy()
df_com['auteur'].iloc[50:100,] = df_cmd['demandeur'].iloc[:50,].copy()
df_com['texte'] =[gen_texte() for x in range(len(df_com))]
df_com['numCommande'].iloc[0:50,] = [x+1 for x in range(50)]
df_com['numCommande'].iloc[50:100,] = [x+1 for x in range(50)]

#Peuplement de la table commentaire
peupler(df_com,'Commentaire')


"""
Création et peuplement de la table Facture
"""

df_fac = pd.DataFrame(columns =['numCommande','adresseFacturation','total'], index=range(100))
df_fac['numCommande'].iloc[:50,] = [x+50 for x in range(50)]
df_fac['numCommande'].iloc[50:100,] = [x+50 for x in range(50)]
df_fac['adresseFacturation'].iloc[:50,]= df_cmd['adresseLivraison'].iloc[50:100,].copy()
df_fac['adresseFacturation'].iloc[50:100,]= df_cmd['adresseLivraison'].iloc[50:100,].copy()
df_fac['total'].iloc[:50,] = 0.5*(df_cmd['prix'].iloc[50:100,].copy())
df_fac['total'].iloc[50:100,] = 0.5*(df_cmd['prix'].iloc[50:100,].copy())

#Peuplement de la table facture
peupler(df_fac,'Facture')