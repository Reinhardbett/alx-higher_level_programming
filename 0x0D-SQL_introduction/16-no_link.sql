-- list all records of table
-- avoid rows without a name value
-- order records in descending manner
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC, name DESC;
