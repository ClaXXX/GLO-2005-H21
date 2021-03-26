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

-- Contrainte pour empêcher un artiste de supprimer son compte client s'il a des commandes en cours
DELIMITER //
CREATE TRIGGER artisteCmdEnCours
    BEFORE DELETE ON Artiste
    FOR EACH ROW
    BEGIN
        IF  OLD.nom IN (SELECT C.superviseur FROM Commande C WHERE C.statut = 'En cours')
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT =  'Supression du compte artiste interdite: commandes en cours';
                END IF;
        END;//
DELIMITER ;

-- Contrainte pour empêcher un client de suprimer son compte alors qu'il a une cmd en cours
DELIMITER //
CREATE TRIGGER clientCmdEnCours
    BEFORE DELETE ON Client
    FOR EACH ROW
    BEGIN
        IF  OLD.courriel IN (SELECT C.demandeur FROM Commande C WHERE C.statut = 'En cours')
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT =  'Supression du compte client interdite: commandes en cours';
                END IF;
        END;//
DELIMITER ;
