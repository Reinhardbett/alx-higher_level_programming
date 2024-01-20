-- List all genres where title = Dexter
-- Add only column tv_genres.name
-- Sort in ascending manner by genre name
SELECT g.`name` AS 'name'
FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s
    ON g.`id` = s.`genre_id`
    INNER JOIN tv_shows AS t
    ON s.`show_id` = t.`id`
WHERE t.`title` = 'Dexter'
ORDER BY `name`;
