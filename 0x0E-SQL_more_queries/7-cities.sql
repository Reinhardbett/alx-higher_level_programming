-- Create the database 'hbtn_0d_usa' only if it doesn't exist
-- Create the table 'cities' only if it doesn't exist
-- Add id that is a primary key
-- Add state_id that is a foreign key
-- Add name that cannot be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities`(
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL,
    PRIMARY KEY(`id`),
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`)
    REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
