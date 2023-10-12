
# how to create database

import mysql.connector


db1 = mysql.connector.connect(password='root',host='localhost',user='root')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()

db2.execute('create database meow')

print('created databaseName :',db2)
# created databaseName : CMySQLCursor: create database meow



# mysql.connector.errors.DatabaseError: 1007 (HY000): Can't create database 'meow'; database exists
