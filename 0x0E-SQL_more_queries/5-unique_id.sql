-- create table unique_id
-- the id column must be unique and have default value 1
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
