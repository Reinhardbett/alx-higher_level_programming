-- list all shows contained shows and genre_id table
-- include shows not featured in genre_id table
SELECT s.title, g.genre_id
FROM tv_shows AS s
    LEFT OUTER JOIN tv_show_genres AS g
    ON s.id = g.show_id
ORDER BY s.title ASC, g.genre_id;
