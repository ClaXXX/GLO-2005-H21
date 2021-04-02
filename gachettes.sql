-- Contrainte de spécialisation
DELIMITER //
CREATE TRIGGER devenirArtiste
    BEFORE INSERT ON Artiste
    FOR EACH ROW
    BEGIN
        IF NOT EXISTS (SELECT courriel FROM Client WHERE courriel = NEW.courriel)
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Vous devez créer un compte client avant de devenir un artiste';
        END IF;
        END;//
DELIMITER ;

-- Contrainte de domaine pour attribut courriel de Client
DELIMITER //
CREATE TRIGGER estCourriel
    BEFORE INSERT ON Client
    FOR EACH ROW
    BEGIN
        IF  (NEW.courriel NOT LIKE '%@%')
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT =  'Le courriel que vous avez entré est invalide';
                END IF;
        END;//
DELIMITER ;

-- Contrainte pour empêcher un artiste de supprimer son compte client s'il a passé au moins une commande
DELIMITER //
CREATE TRIGGER artisteCmd
    BEFORE DELETE ON Artiste
    FOR EACH ROW
    BEGIN
        IF  OLD.nom IN (SELECT C.superviseur FROM Commande C)
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT =  'Supression du compte artiste interdite: commandes en cours';
                END IF;
        END;//
DELIMITER ;

-- Contrainte pour empêcher un client de supprimer son compte alors qu'il a passé au moins une cmd
DELIMITER //
CREATE TRIGGER clientCmd
    BEFORE DELETE ON Client
    FOR EACH ROW
    BEGIN
        IF  OLD.courriel IN (SELECT C.demandeur FROM Commande C)
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT =  'Supression du compte client interdite: commandes en cours';
                END IF;
        END;//
DELIMITER ;

-- Création d'un tuple oeuvre lorsqu'une commande de type Création est passée
DELIMITER //
CREATE TRIGGER nouvOeuvre
    BEFORE INSERT ON Commande
    FOR EACH ROW
    BEGIN
        IF  NEW.oeuvre  NOT IN (SELECT O.nom FROM Oeuvre O) AND NEW.type = 'création'
        THEN
            INSERT INTO Oeuvre(nom,auteur) VALUES (NEW.oeuvre, NEW.superviseur);
                END IF;
        END;//
DELIMITER ;

