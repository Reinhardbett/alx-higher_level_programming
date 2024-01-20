-- List all shows in 'hbtn_0d_tvshows'
-- Display tv_shows.title - tv_show_genres.genre_id
-- If show has no genre, display NULL
-- Order by tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
    LEFT JOIN `tv_show_genres` AS g
    ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
