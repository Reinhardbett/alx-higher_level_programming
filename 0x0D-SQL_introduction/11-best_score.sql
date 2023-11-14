-- list all records in second_table where score >= 10
-- Display only score and name respectively
-- Order records by score in descending manner
SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
