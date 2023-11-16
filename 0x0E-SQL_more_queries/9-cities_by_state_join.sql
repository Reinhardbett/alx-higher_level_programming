-- expand all state_id foreign keys to respective states
-- display cities.id, cities.name, states.name
-- sort results in ascending order by cities.id
SELECT c.id, c.name, s.name
FROM cities AS c
    INNER JOIN states AS s
    ON c.state_id = s.id
ORDER BY c.id ASC;

