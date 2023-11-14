-- list number of records with same score
-- place the corresponding number of records in a new column
-- order number of records in a descending manner
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
HAVING COUNT(score) >= 1
