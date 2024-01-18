-- Create database 'hbtn_0d_usa' only if doesn't exist
-- Create table 'states' only if doesn't exist
-- Add attribute id and name
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states`(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    PRIMARY KEY(`id`),
    name VARCHAR(256)
);
