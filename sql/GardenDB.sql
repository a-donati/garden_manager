DROP DATABASE IF EXISTS `garden`;
CREATE DATABASE IF NOT EXISTS `garden`;
USE `garden`;

DROP TABLE IF EXISTS `Users`;

CREATE TABLE `Users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `is_active` TINYINT(1) DEFAULT 1,
  PRIMARY KEY (`user_id`)
);

DROP TABLE IF EXISTS `Gardens`;

CREATE TABLE `Gardens` (
  `garden_id` int NOT NULL AUTO_INCREMENT,
  `garden_name` VARCHAR(50) NOT NULL,
  `owner_id` INT,
  FOREIGN KEY (owner_id) REFERENCES Users(user_id) ON DELETE SET NULL,
  PRIMARY KEY (`garden_id`),
  UNIQUE (`garden_name`, `owner_id`)  -- Enforces uniqueness of garden name per user
);

DROP TABLE IF EXISTS `Plants`;

CREATE TABLE `Plants` (
    plant_id INT AUTO_INCREMENT,
    plant_name VARCHAR(100) NOT NULL,
    plant_type ENUM('Flower', 'Vegetable') NOT NULL,
    image_path VARCHAR(255) NULL,
    PRIMARY KEY (`plant_id`)
);

DROP TABLE IF EXISTS `User_Garden`;

CREATE TABLE `User_Garden` (
    user_id INT,
    garden_id INT,
    PRIMARY KEY (user_id, garden_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (garden_id) REFERENCES Gardens(garden_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS `Garden_Plants`;

CREATE TABLE `Garden_Plants` (
    garden_id INT,
    plant_id INT,
    user_id INT,
    date_added DATE NOT NULL,
    quantity INT UNSIGNED NOT NULL DEFAULT 1, 
    PRIMARY KEY (garden_id, plant_id, user_id),  
    FOREIGN KEY (garden_id) REFERENCES Gardens(garden_id) ON DELETE CASCADE,
    FOREIGN KEY (plant_id) REFERENCES Plants(plant_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Sample Data for Users
INSERT INTO Users (username, password, is_active) VALUES ('user1', 'password1', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user2', 'password2', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user3', 'password3', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user4', 'password4', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user5', 'password5', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user6', 'password6', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user7', 'password7', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user8', 'password8', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user9', 'password9', 1);
INSERT INTO Users (username, password, is_active) VALUES ('user10', 'password10', 1);

-- Sample Data for Gardens
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Rose Garden', 1);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Vegetable Patch', 1);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Flower Bed', 2);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Herb Garden', 3);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Orchard', 4);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Cactus Garden', 5);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Tropical Paradise', 6);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Zen Garden', 7);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Community Garden', 8);
INSERT INTO Gardens (garden_name, owner_id) VALUES ('Butterfly Garden', 9);

-- Sample Data for Plants
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Rosa', 'Flower', 'images/rosa.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Tomato', 'Vegetable', 'images/tomato.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Tulip', 'Flower', 'images/tulip.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Basil', 'Vegetable', 'images/basil.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Apple Tree', 'Vegetable', 'images/apple_tree.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Sunflower', 'Flower', 'images/sunflower.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Carrot', 'Vegetable', 'images/carrot.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Lettuce', 'Vegetable', 'images/lettuce.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Daisy', 'Flower', 'images/daisy.jpg');
INSERT INTO Plants (plant_name, plant_type, image_path) VALUES ('Mint', 'Vegetable', 'images/mint.jpg');

-- Sample Data for User_Garden
INSERT INTO User_Garden (user_id, garden_id) VALUES (1, 1);
INSERT INTO User_Garden (user_id, garden_id) VALUES (1, 2);
INSERT INTO User_Garden (user_id, garden_id) VALUES (2, 1);
INSERT INTO User_Garden (user_id, garden_id) VALUES (3, 3);
INSERT INTO User_Garden (user_id, garden_id) VALUES (4, 4);
INSERT INTO User_Garden (user_id, garden_id) VALUES (5, 5);
INSERT INTO User_Garden (user_id, garden_id) VALUES (6, 6);
INSERT INTO User_Garden (user_id, garden_id) VALUES (7, 7);
INSERT INTO User_Garden (user_id, garden_id) VALUES (8, 8);
INSERT INTO User_Garden (user_id, garden_id) VALUES (9, 9);
INSERT INTO User_Garden (user_id, garden_id) VALUES (10, 10);

-- Additional Sample Data for Garden_Plants
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (1, 1, 1, '2025-05-07', 5);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (2, 2, 1, '2025-05-07', 10);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (1, 3, 2, '2025-05-08', 3);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (4, 4, 3, '2025-05-09', 7);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (5, 5, 4, '2025-05-10', 2);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (6, 6, 5, '2025-05-11', 4);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (7, 7, 6, '2025-05-12', 6);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (8, 8, 7, '2025-05-13', 2);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (9, 9, 8, '2025-05-14', 3);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (10, 1, 9, '2025-05-15', 1);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (1, 2, 10, '2025-05-16', 8);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (2, 3, 1, '2025-05-17', 4);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (3, 4, 2, '2025-05-18', 5);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (4, 5, 3, '2025-05-19', 3);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (5, 6, 4, '2025-05-20', 6);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (6, 7, 5, '2025-05-21', 2);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (7, 8, 6, '2025-05-22', 4);
INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity) VALUES (8, 9, 7, '2025-05-23', 5);

-- Views
CREATE VIEW UserGardens AS
SELECT u.username, g.garden_name
FROM Users u
JOIN User_Garden ug ON u.user_id = ug.user_id
JOIN Gardens g ON ug.garden_id = g.garden_id;
-- VVVV This one below is to view all plants in all gardens, I will use this during my updates
-- CREATE VIEW GetPlantsInGarden AS
-- SELECT g.garden_name, p.plant_name, p.plant_type, p.image_path, gp.date_added, gp.quantity, u.username
-- FROM Gardens g
-- JOIN Garden_Plants gp ON g.garden_id = gp.garden_id
-- JOIN Plants p ON gp.plant_id = p.plant_id
-- JOIN Users u ON gp.user_id = u.user_id;

-- CREATE OR REPLACE VIEW GetPlantsInGarden AS
-- SELECT 
--     g.garden_id,  
--     g.garden_name, 
--     p.plant_name, 
--     p.plant_type, 
--     p.image_path, 
--     gp.date_added, 
--     gp.quantity, 
--     u.user_id,  
--     u.username
-- FROM 
--     Gardens g
-- JOIN 
--     Garden_Plants gp ON g.garden_id = gp.garden_id
-- JOIN 
--     Plants p ON gp.plant_id = p.plant_id
-- JOIN 
--     Users u ON gp.user_id = u.user_id;

CREATE OR REPLACE VIEW GetPlantsInGarden AS
SELECT 
    g.garden_id,  
    g.garden_name, 
    p.plant_name, 
    p.plant_type, 
    p.image_path, 
    gp.date_added, 
    gp.quantity, 
    gp.user_id,   
    u.username
FROM 
    Gardens g
JOIN 
    Garden_Plants gp ON g.garden_id = gp.garden_id
JOIN 
    Plants p ON gp.plant_id = p.plant_id
JOIN 
    Users u ON gp.user_id = u.user_id;


-- View: Aggregate - Count of plants in each garden
CREATE VIEW GardenPlantCounts AS
SELECT g.garden_name, SUM(gp.quantity) AS plant_count
FROM Gardens g
JOIN Garden_Plants gp ON g.garden_id = gp.garden_id
GROUP BY g.garden_name;

-- Functions
-- Function: Get User ID by Username
DELIMITER //
CREATE FUNCTION GetUserId(input_username VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE user_id_val INT;
    SELECT user_id INTO user_id_val FROM Users WHERE username = input_username;
    IF user_id_val IS NULL THEN
        RETURN -1;
    ELSE
        RETURN user_id_val;
    END IF;
END //
DELIMITER ;

-- Function: Get Garden ID by Garden Name
DELIMITER //
CREATE FUNCTION GetGardenId(input_garden_name VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE garden_id_val INT;
    SELECT garden_id INTO garden_id_val FROM Gardens WHERE garden_name = input_garden_name;
    IF garden_id_val IS NULL THEN
        RETURN -1;
    ELSE
        RETURN garden_id_val;
    END IF;
END //
DELIMITER ;

-- Function: Get Plant ID by Plant Name
DELIMITER //
CREATE FUNCTION GetPlantIdByName(input_plant_name VARCHAR(100))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE plant_id_val INT;
    SELECT plant_id INTO plant_id_val FROM Plants WHERE plant_name = input_plant_name;
    IF plant_id_val IS NULL THEN
        RETURN -1;
    ELSE
        RETURN plant_id_val;
    END IF;
END //
DELIMITER ;

-- Stored Procedures

-- Stored Procedure: Authenticate User
DELIMITER //
CREATE PROCEDURE AuthenticateUser(IN username_param VARCHAR(50), IN password_param VARCHAR(50))
BEGIN
    SELECT * FROM Users WHERE username = username_param AND password = password_param;
END //
DELIMITER ;

-- Stored Procedure: Create User
DELIMITER //
CREATE PROCEDURE CreateUser(IN username_param VARCHAR(50), IN password_param VARCHAR(50))
BEGIN
    INSERT INTO Users (username, password) VALUES (username_param, password_param);
END //
DELIMITER ;

-- Stored Procedure: Add Garden
DELIMITER //
CREATE PROCEDURE AddGarden(garden_name_param VARCHAR(50), owner_id_param INT)
BEGIN
    INSERT INTO Gardens (garden_name, owner_id) VALUES (garden_name_param, owner_id_param);
END //
DELIMITER ;

-- Stored Procedure: Add User to Garden
DELIMITER //
CREATE PROCEDURE AddUserToGarden(user_id_param INT, garden_id_param INT)
BEGIN
    INSERT INTO User_Garden (user_id, garden_id)
    VALUES (user_id_param, garden_id_param)
    ON DUPLICATE KEY UPDATE garden_id = garden_id_param; 
END //
DELIMITER ;
-- Stored Procedure: Get Users associated with gardens
DELIMITER $$

CREATE PROCEDURE GetGardenUsers(IN garden_name VARCHAR(255))
BEGIN
    -- Select users associated with the specified garden name
    SELECT u.username
    FROM Users u
    JOIN User_Garden ug ON u.user_id = ug.user_id
    JOIN Gardens g ON ug.garden_id = g.garden_id
    WHERE g.garden_name = garden_name;
END$$

DELIMITER ;

-- Stored Procedure: Add Plant to Garden
-- DELIMITER //
-- CREATE PROCEDURE AddPlantToGarden(
--     IN garden_id_param INT,
--     IN plant_id_param INT,
--     IN user_id_param INT,
--     IN date_added_param DATE,
--     IN quantity_param INT UNSIGNED
-- )
-- BEGIN
--     -- Check if the plant already exists in the garden for the user
--     IF EXISTS (SELECT 1 FROM Garden_Plants WHERE garden_id = garden_id_param AND plant_id = plant_id_param AND user_id = user_id_param) THEN
--         -- If the plant exists, update the quantity
--         UPDATE Garden_Plants
--         SET quantity = quantity + quantity_param
--         WHERE garden_id = garden_id_param AND plant_id = plant_id_param AND user_id = user_id_param;
--     ELSE
--         -- If the plant does not exist, add it to the garden
--         INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity)
--         VALUES (garden_id_param, plant_id_param, user_id_param, date_added_param, quantity_param);
--     END IF;
-- END //
-- DELIMITER ;
DELIMITER //
CREATE PROCEDURE AddPlantToGarden(
    IN garden_id_param INT,
    IN plant_name_param VARCHAR(100),
    IN plant_type_param VARCHAR(100),
    IN user_id_param INT,
    IN date_added_param DATE,
    IN quantity_param INT UNSIGNED
)
BEGIN
    DECLARE plant_id_param INT;

    -- Check if the plant already exists
    SELECT plant_id INTO plant_id_param 
    FROM Plants 
    WHERE plant_name = plant_name_param AND plant_type = plant_type_param;

    -- If the plant exists, update the quantity in Garden_Plants
    IF plant_id_param IS NOT NULL THEN
        IF EXISTS (SELECT 1 FROM Garden_Plants WHERE garden_id = garden_id_param AND plant_id = plant_id_param AND user_id = user_id_param) THEN
            -- If the plant exists in the garden, update the quantity
            UPDATE Garden_Plants
            SET quantity = quantity + quantity_param
            WHERE garden_id = garden_id_param AND plant_id = plant_id_param AND user_id = user_id_param;
        ELSE
            -- If the plant does not exist in the garden, add it to the garden
            INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity)
            VALUES (garden_id_param, plant_id_param, user_id_param, date_added_param, quantity_param);
        END IF;
    ELSE
        -- If the plant does not exist, create a new plant entry
        INSERT INTO Plants (plant_name, plant_type, image_path)
        VALUES (plant_name_param, plant_type_param, NULL);  -- Set image_path to NULL if not provided

        -- Get the new plant's ID
        SET plant_id_param = LAST_INSERT_ID();

        -- Now add the new plant to the garden
        INSERT INTO Garden_Plants (garden_id, plant_id, user_id, date_added, quantity)
        VALUES (garden_id_param, plant_id_param, user_id_param, date_added_param, quantity_param);
    END IF;
END //
-- DROP PROCEDURE IF EXISTS RemovePlantFromGarden;
-- CREATE PROCEDURE RemovePlantFromGarden(
--     IN garden_id_param INT,
--     IN plant_id_param INT,
--     IN user_id_param INT
-- )
-- BEGIN
--     DELETE FROM Garden_Plants
--     WHERE garden_id = garden_id_param
--       AND plant_id = plant_id_param
--       AND user_id = user_id_param;
-- END

-- DELIMITER //

-- CREATE PROCEDURE RemovePlantFromGarden(
--     IN garden_name_param VARCHAR(50),
--     IN plant_name_param VARCHAR(100),
--     IN username_param VARCHAR(50)
-- )
-- BEGIN
--     DECLARE garden_id_val INT;
--     DECLARE plant_id_val INT;
--     DECLARE user_id_val INT;

--     -- Get the IDs from names
--     SET garden_id_val = GetGardenId(garden_name_param);
--     SET plant_id_val = GetPlantIdByName(plant_name_param);
--     SET user_id_val = GetUserId(username_param);

--     -- Delete the entry from Garden_Plants
--     DELETE FROM Garden_Plants
--     WHERE garden_id = garden_id_val
--       AND plant_id = plant_id_val
--       AND user_id = user_id_val;
-- END //

-- DELIMITER ;

DELIMITER //
CREATE PROCEDURE RemovePlantFromGarden(IN g_id INT, IN p_id INT, IN u_id INT)
BEGIN
    DELETE FROM garden_plants
    WHERE garden_id = g_id AND plant_id = p_id AND user_id = u_id;
END //
DELIMITER ;

-- Stored Procedure: Update Plant
DELIMITER //
CREATE PROCEDURE UpdatePlant(
    plant_id_param INT,
    plant_name_param VARCHAR(100),
    plant_type_param ENUM('Flower', 'Vegetable'),
    image_path_param VARCHAR(255)
)
BEGIN
    UPDATE Plants
    SET plant_name = plant_name_param,
        plant_type = plant_type_param,
        image_path = image_path_param
    WHERE plant_id = plant_id_param;
END //
DELIMITER ;

-- Call Views and Procedures
SELECT * FROM UserGardens;
SELECT * FROM GetPlantsInGarden;
SELECT * FROM GardenPlantCounts;

-- Function Calls
SELECT GetUserId('user1');
SELECT GetUserId('nonexistentuser');
SELECT GetGardenId('Rose Garden');
SELECT GetGardenId('nonexistentgarden');
SELECT GetPlantIdByName('Rosa');
SELECT GetPlantIdByName('nonexistentplant');

-- Procedure Calls
CALL AddGarden('New Garden', 1);
CALL AddUserToGarden(2, 1);

-- CALL UpdatePlant(1, 'Rosa Updated', 'Flower', 'images/rosa_updated.jpg');
-- CALL RemovePlantFromGarden(1);

-- Final View Calls
-- SELECT * FROM UserGardens;
-- SELECT * FROM GetPlantsInGarden;
-- SELECT * FROM GardenPlantCounts;

-- DROP PROCEDURE IF EXISTS RemoveUserFromGarden;

-- DELIMITER //
-- CREATE PROCEDURE RemoveUserFromGarden(IN userId INT, IN gardenId INT)
-- BEGIN
--     DELETE FROM user_garden 
--     WHERE user_id = userId AND garden_id = gardenId;
-- END //

-- DELIMITER ;
DROP PROCEDURE IF EXISTS RemoveUserFromGarden;

DELIMITER //
CREATE PROCEDURE RemoveUserFromGarden(IN userId INT, IN gardenId INT)
BEGIN
    DELETE FROM user_garden 
    WHERE user_id = userId AND garden_id = gardenId;
    
    IF ROW_COUNT() > 0 THEN
        SELECT 'Success: User removed.' AS result;
    ELSE
        SELECT 'Error: No user found with the specified ID in this garden.' AS result;
    END IF;
END //
DELIMITER ;
