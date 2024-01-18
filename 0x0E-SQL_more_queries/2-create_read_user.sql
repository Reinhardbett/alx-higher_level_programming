-- Create database 'hbtn_0d_2' only if it doesn't exist
-- Create user 'user_0d_2' only if doesn't exist
-- Set user 'user_0d_2' to have only SELECT privilege on hbtn_0d_2
-- Set user 'user_0d_2' password to 'user_0d_2_pwd'
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;
CREATE USER
    IF NOT EXISTS `user_0d_2`@`localhost`
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
    ON `hbtn_0d_2`.*
    TO `user_0d_2`@`localhost`;
