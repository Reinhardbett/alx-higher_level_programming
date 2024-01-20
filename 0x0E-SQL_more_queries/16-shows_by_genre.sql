 -- List all shows and all genres linked
 -- Display 'tv_shows.title' - 'tv_genres.name'
 -- Order by show title in ascending manner
SELECT s.`title` AS `title`, g.`name` AS `name`
FROM `tv_shows` AS s
    LEFT JOIN `tv_show_genres` AS t
    ON s.`id` = t.`show_id`
    LEFT JOIN `tv_genres` as g
    ON t.`genre_id` = g.`id`
ORDER BY `title`, `name`;
