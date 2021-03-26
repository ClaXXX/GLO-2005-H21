CREATE DATABASE ${SQL_DB};
USE ${SQL_DB};

CREATE TABLE Oeuvre(
    nom varchar(32),
    auteur varchar(32),
    dateCreation date,
    type varchar(16),
    description varchar(256),
    enExposition int(1),
    PRIMARY KEY(nom, auteur),
    FOREIGN KEY (auteur)
        REFERENCES Artiste(nom)
);

CREATE TABLE Facture(
    numFacture integer AUTO_INCREMENT PRIMARY KEY,
    numCommande integer,
    adresseLivraison varchar(64),
    adresseFacturation varchar(64),
    total double(6,2),
    FOREIGN KEY(numCommande)
        REFERENCES Commande(num)
);

CREATE TABLE Commande(
    num integer AUTO_INCREMENT PRIMARY KEY,
    superviseur  varchar(32),
    demandeur varchar(32),
    statut enum('En cours', 'Complétée', 'En attente de confirmation', 'Annulée'),
    prix double(6,2),
    type enum('Création', 'Réservation'),
    FOREIGN KEY(superviseur)
        REFERENCES Artiste(nom),
    FOREIGN KEY(demandeur)
        REFERENCES Client(courriel)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE Commentaire(
    auteur varchar(32),
    numCommande integer,
    texte varchar(128),
    date timestamp
);

CREATE TABLE Client(
    courriel varchar(64) PRIMARY KEY,
    motPasse varchar(32),
    nom varchar(32),
    prenom varchar(32),
    adresse varchar(64)
);

CREATE TABLE Artiste(
    courriel varchar(64) PRIMARY KEY,
    nom varchar(32) UNIQUE,
    FOREIGN KEY(courriel)
        REFERENCES Client(courriel)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
