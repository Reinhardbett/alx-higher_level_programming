-- create database hbtn_0d_usa
-- create table cities within the database hbtn_0_usa
-- create attibute id
-- create attribute state_id which must be a FOREIGN KEY that references to id of the states table
-- create attribute name
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE
    IF NOT EXISTS cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    PRIMARY KEY (id),
    state_id INT NOT NULL,
    FOREIGN KEY (state_id)
    REFERENCES states(id),
    name VARCHAR(256) NOT NULL
    );
