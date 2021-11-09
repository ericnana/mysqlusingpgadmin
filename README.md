# Goals
The aim of this is to be able to use a python script to play with all what SQL has to offer like query data from table,
using SQL operators, managing views, tables so on and so forth,

# How to get there
I used pgadmin4 in this instance.
Used as well the command line on my unix system.
Create a Server directly from the GUI and afterwards created a database as well.
After these two ran the python scripts to perform all sort of queries needed.

# More
Connect to Postgres from cammand line
sudo -i -u postgres --> psql

In order to create a database after setting the server from pgadmin gui you do the following from command line:
CREATE USER postgres_user WITH PASSWORD 'password';
CREATE DATABASE my_postgres_db OWNER postgres_user;
\q
exit
sudo su - postgres_user

To get into the database from the console from the start as user: sudo su - postgres_user --> psql my_postgres_db
Then you are switched to the desired database. Afterwards you can start modifying or create whatever you want.

To drop a databse do the following:
kill the server from the pgadmin icon and do the login again into your console from the start as user:
sudo -i -u postgres -> psql -->'postgres=# drop database name_of_the_database;' or DROP DATABASE name_of_the_database;

To Grant privileges:
psql -d my_postgres_db
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres_user;

