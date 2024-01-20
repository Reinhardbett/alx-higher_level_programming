-- List all shows in 'hbtn_0d_tvshows' linked to at least a genre
-- Display tv_shows.title - tv_show_genres.genre_id
-- Order by tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
    INNER JOIN `tv_show_genres` AS g
    ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
