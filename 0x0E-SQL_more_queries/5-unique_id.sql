-- Create table 'unique_id' only if doesn't exist
-- Add attributes id that must be unique and name
CREATE TABLE IF NOT EXISTS `unique_id`(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
