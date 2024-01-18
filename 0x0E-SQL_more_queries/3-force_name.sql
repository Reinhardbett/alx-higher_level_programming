-- Create table 'force_name' if doesn't exist
-- Add attributes id and name that can't be empty
CREATE TABLE IF NOT EXISTS `force_name`(
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);
