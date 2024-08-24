import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

my_cursor = mydb.cursor()
#which is used to do perform commands like robots
# my_cursor.execute("CREATE DATABASE our_users1")
#it will not going to create database again if we didnt comment it only once

my_cursor.execute("SHOW DATABASES")
#this will show all the databases in the server
for db in my_cursor:
    print(db)