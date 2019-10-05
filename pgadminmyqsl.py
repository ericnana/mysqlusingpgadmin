
import psycopg2
from psycopg2 import Error


	
#CREATE DATABASE userdatabase;

try:
    connection = psycopg2.connect(host = "localhost", user = "YOUR_USERNAME", password = "YOUR_PASSWORD", port = "YOUR_PORT", database = "YOUR_CREATED_DATABASE")
    cursor = connection.cursor()
    
    #CREATE TABLE
    create_table_query = '''CREATE TABLE mobile
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE           REAL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
