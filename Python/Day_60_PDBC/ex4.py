# How to create table
import mysql.connector


db1 = mysql.connector.connect(password='root',host='localhost',user='root',database='meow')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()


Table = "create table emp(sno int, fname varchar(30), lname varchar(30), salary int,location varchar(30))"


db2.execute(Table)

print(db2)

# CMySQLCursor: create table emp(sno int, fname varchar(..
