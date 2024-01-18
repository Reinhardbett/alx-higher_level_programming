-- List all cities of California
-- Use database 'hbtn_0d_usa'
-- Order in ascending manner by id
USE `hbtn_0d_usa`;
SELECT id, name
FROM `cities`
WHERE `state_id` = 1
ORDER BY id ASC;
