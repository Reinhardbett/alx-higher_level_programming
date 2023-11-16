-- list all attributes from table cities with foreign key id of California
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id ASC;
