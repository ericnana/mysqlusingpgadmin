# Goals
The aim of this is to be able to use a script python to play with all what SQL has to offer like query data from table,
using SQL operators, managing views, tables so on and so forth,

# How to get there
I used pgadmin4 in this instance
Used as well the command line on my unix system
Create a Server directly from the GUI and afterwards created a database as well.
After these two ran the python scripts to perform all sort of queries needed.

# More
Connect to Postgres from cammand line
sudo -i -u postgres --> psql

In order to create a database after setting the server from pgadmin gui you do  the following:
CREATE USER postgres_user WITH PASSWORD 'password';
CREATE DATABASE my_postgres_db OWNER postgres_user;
\q
exit
sudo su - postgres_user

To sign into database from the console: sudo su - postgres_user --> psql my_postgres_db
Then you are switched to the desired database

To drop a databse do the following:
kill the server from the pgadmin icon and do the login again into your console from the start
sudo -i -u postgres -> psql -->'postgres=# drop database name_of_the_database;' or DROP DATABASE name_of_the_database;

To Grant privileges:
psql -d yourDBName
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO userName;

