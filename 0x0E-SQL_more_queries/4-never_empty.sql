-- Create table 'id_not_null' only if doesn't exist
-- Add attributes id with default value 1 and name
CREATE TABLE IF NOT EXISTS `id_not_null`(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
