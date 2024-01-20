 -- List all Comedy shows
 -- Display 'tv_shows.title'
 -- Ordery by show title in ascending manner
SELECT s.`title` AS `title`
FROM `tv_shows` AS s
    INNER JOIN `tv_show_genres` AS t
    ON s.`id` = t.`show_id`
    INNER JOIN `tv_genres` as g
    ON t.`genre_id` = g.`id`
WHERE g.`name` = 'Comedy'
ORDER BY `title`
