-- a script that lists all privileges of the MySQL users
-- and user_0d_2 on your server (in localhost).
-- connect to he mysql server
mysql -u root -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
