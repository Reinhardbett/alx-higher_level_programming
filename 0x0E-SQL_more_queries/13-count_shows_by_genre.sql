-- List all genres from 'hbtn_0d_tvshows'
-- Display the number of shows linked to each genre
-- First column must be called 'genre'
-- Second column must be called 'number_of_shows'
-- Do not display a genre that does not have any shows linked
-- Order by number of shows linked in descending manner
SELECT g.`name` AS 'genre', COUNT(*) AS 'number_of_shows'
FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s
    ON g.`id` = s.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;
