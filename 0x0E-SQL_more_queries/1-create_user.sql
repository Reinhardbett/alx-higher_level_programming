-- Create user user_0d_1 only if does not exist
-- Grant all privileges
-- Set user password to 'user_0d_1_pwd'
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES 
    ON *.* 
    TO 'user_0d_1'@'localhost';
