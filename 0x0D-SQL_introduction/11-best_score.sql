-- List all records where the score column has value >= 10
-- Results should displays score and name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
