-- List all records in table second_table
-- Select only those with score above or equal to 10
-- Display score, name respectively 
-- Order by score
SELECT score, name
FROM `second_table`
WHERE score >= 10
ORDER BY score DESC;
