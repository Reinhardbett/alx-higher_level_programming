-- Create table second_table only if it doesn't exist
-- Add columns id INT, name VARCHAR(256), score INT
-- Insert values 1, "John", 10
-- Insert values 2, "Alex", 3
-- Insert values 3, "Bob", 14
-- Insert values 4, "George", 8
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO `second_table` VALUES(1, "John", 10);
INSERT INTO `second_table` VALUES(2, "Alex", 3);
INSERT INTO `second_table` VALUES(3, "Bob", 14);
INSERT INTO `second_table` VALUES(4, "George", 8);
