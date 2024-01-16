-- List all records of score and name in table second_table
-- Attribute name must have a value
-- Order records in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
