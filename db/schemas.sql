CREATE DATABASE IF NOT EXISTS tp DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE tp;

CREATE TABLE IF NOT EXISTS Client(
    courriel varchar(64) PRIMARY KEY,
    mdp varchar(256) NOT NULL,
    nom varchar(32),
    prenom varchar(32),
    adresse varchar(64)
);

CREATE TABLE IF NOT EXISTS Artiste(
    courriel varchar(64) PRIMARY KEY,
    nom varchar(32) UNIQUE NOT NULL,
    FOREIGN KEY(courriel)
        REFERENCES Client(courriel)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Oeuvre(
    nom varchar(64) NOT NULL,
    auteur varchar(32) NOT NULL,
    dateCreation date,
    type varchar(16),
    description varchar(256),
    enExposition int(1) DEFAULT FALSE,
    PRIMARY KEY(nom, auteur),
    FOREIGN KEY (auteur)
        REFERENCES Artiste(nom)
);

CREATE TABLE IF NOT EXISTS Commande(
    num integer AUTO_INCREMENT PRIMARY KEY,
    oeuvre varchar(64),
    superviseur varchar(64) NOT NULL,
    demandeur varchar(64) NOT NULL,
    statut enum('En cours', 'Complétée', 'En attente de confirmation', 'Annulée') DEFAULT 'En cours',
    prix double(6,2),
    type enum('Création', 'Réservation') NOT NULL,
    adresseLivraison varchar(64),
    FOREIGN KEY(oeuvre)
        REFERENCES Oeuvre(nom),
    FOREIGN KEY(superviseur)
        REFERENCES Artiste(nom),
    FOREIGN KEY(oeuvre)
        REFERENCES Oeuvre(nom),
    FOREIGN KEY(demandeur)
        REFERENCES Client(courriel)
            ON DELETE NO ACTION
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Facture(
    numFacture integer AUTO_INCREMENT PRIMARY KEY,
    numCommande integer NOT NULL,
    adresseFacturation varchar(64) NOT NULL,
    total double(6,2) NOT NULL,
    FOREIGN KEY(numCommande)
        REFERENCES Commande(num)
);

CREATE TABLE IF NOT EXISTS Commentaire(
    id integer AUTO_INCREMENT PRIMARY KEY,
    auteur varchar(64) NOT NULL,
    numCommande integer NOT NULL,
    texte varchar(128) NOT NULL,
    creation date DEFAULT (CURRENT_DATE),
    FOREIGN KEY(auteur)
        REFERENCES Client(courriel),
    FOREIGN KEY(numCommande)
        REFERENCES Commande(num)
);