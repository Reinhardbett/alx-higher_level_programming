-- List all cities in database 'hbtn_0d_usa`
-- Display according to cities.id-cities.name-states.name
-- Order by cities.id
SELECT c.`id`, c.`name`, s.`name`
FROM `cities` AS c
    INNER JOIN `states` AS s
    ON c.`state_id` = s.`id`
ORDER BY c.`id`;
