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

# Connection à la bd pour peupler les tables
load_dotenv()
db = DataBase(getenv('SQL_HOST'), getenv('SQL_USER'), getenv('SQL_PASSWORD'), getenv('SQL_DB'))
curseur = db.cursor()

def peupler(df, nom_table):
    cols = ",".join([str(i) for i in df.columns.tolist()])  # str des attributs à insérer dans la déclaration SQL
    for i, rang in df.iterrows():
        cmd = "INSERT INTO "+ nom_table+" (" + cols + " ) VALUES (" + "%s," * (len(rang) - 1) + "%s)"
        curseur.execute(cmd, tuple(rang))
    return cmd

"""
Création et peuplement de la table Client
"""
# Création des mot de passes clients
def gen_MP():
    lettres = string.ascii_letters
    chiffres = string.digits
    chars = lettres + chiffres
    motpasse = "".join(random.choice(chars) for x in range(random.randint(16, 32)))
    return motpasse
# création d'un dataframe Client via lecture du fichier .csv contenant noms accentués
df = pd.read_csv('nomClient2.csv', encoding='latin1')

#Concaténation de l'adresse
df['adresse'] = df['adresse_rue'] + ', ' + df['ville'] +' '+  df['code_postal']
df.drop(['adresse_rue','ville','code_postal'],axis=1,inplace=True)

# Création des adresses courriels à partir des nom et prénom des clients
df = df.assign(courriel = df['prenom'] + '.' + df['nom'])
df['courriel'] =df['courriel'].apply(lambda x: uni.unidecode(x.lower()) + '@gmail.com') #création du courriel sans accents et en minuscule

#Création de la colonne motPasse
df = df.assign(motPasse=[gen_MP() for x in range(len(df))])
#print(df2['motPasse'])

#Peuplement de la table Client
cols = ",".join([str(i) for i in df.columns.tolist()]) #str des attributs à insérer dans la déclaration SQL

for i, rang in df.iterrows():
    cmd_sql = "INSERT INTO Client (" + cols+" ) VALUES (" + "%s,"*(len(rang)-1) + "%s)"
   # curseur.execute(cmd_sql, tuple(rang))

"""
Création et peuplement de la table Artiste
"""
# création du dataframe Artiste
df_a = df[['courriel']].iloc[0:99].copy()
df_a = df_a.assign(nom= df['prenom'].apply(lambda x: x[0:3]) + df['nom'].apply(lambda x: x[0:3])) #nomArtiste : concat des 3 premières lettres du prenom et nom
df_a['nom'] = df_a['nom'].apply(lambda x: x.lower())
print(df_a)

#Peuplement de la table
#peupler(df_a,'Artiste')

#cols_art = ",".join([str(i) for i in df_a.columns.tolist()])
#print(cols_art)
#for i, rang in df_a.iterrows():
    #cmd_sql = "INSERT INTO Artiste (" + cols_art+" ) VALUES (" + "%s,"*(len(rang)-1) + "%s)"
    #curseur.execute(cmd_sql, tuple(rang))


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
    phrase = lorem.get_sentence(count=2, comma=(0, 2), word_range=(4, 8))
    return phrase

#Création du dataframe oeuvre
df_oeu = pd.read_csv('nomOeuvre.csv', encoding='latin1')
df_oeu = df_oeu.assign(auteur=df_a['nom'].iloc[:99,])
df_oeu['auteur'].iloc[100:126] = df_a['nom'].iloc[:26,]
df_oeu = df_oeu.assign(dateCreation=[gen_date() for x in range(len(df_oeu))])
df_oeu = df_oeu.assign(type=[type_oeuvre() for x in range(len(df_oeu))])
df_oeu = df_oeu.assign(description=[desc_oeuvre() for x in range(len(df_oeu))])
df_oeu = df_oeu.assign(enExposition=[random.randint(0,1) for x in range(len(df_oeu))])

#Peuplement de la table

#peupler(df_oeu,'Oeuvre')

