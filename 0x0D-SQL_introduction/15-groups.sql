 -- List number of records with same score in table second_table
 -- Display score and number of records for each score as number
 -- Order by number in descending manner
 SELECT `score`, COUNT(*) AS number
 FROM `second_table`
 GROUP BY `score`
 ORDER BY `number` DESC;
