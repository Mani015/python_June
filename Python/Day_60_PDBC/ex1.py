
# MySQL Connector Python

# Advantages and benefits of MySQL Connector Python: –
#
# MySQL Connector Python is written in pure Python, and it is self-sufficient to execute database queries through Python.
# It is an official Oracle-supported driver to work with MySQL and Python.

# How to connect MySQL database in Python
# Let’s see how to connect the MySQL database in Python using the ‘MySQL Connector Python’ module.
#
# Arguments required to connect
# You need to know the following detail of the MySQL server to perform the connection from Python.
#
# Argument	Description
# Username	The username that you use to work with MySQL Server. The default username for the MySQL database is a root.
# Password	Password is given by the user at the time of installing the MySQL server. If you are using root then you won’t need the password.
# Host name	The server name or Ip address on which MySQL is running. if you are running on localhost, then you can use localhost or its IP 127.0.0.0
# Database name	The name of the database to which you want to connect and perform the operations.
#
# How to Connect to MySQL Database in Python
#
# Install MySQL connector module
# Use the pip command to install MySQL connector Python.
# pip install mysql-connector-python
#
# Import MySQL connector module
# Import using a import mysql.connector statement so you can use this module’s methods to communicate with the MySQL database.
#
# Use the connect() method
# Use the connect() method of the MySQL Connector class with the required arguments to connect MySQL. It would return a MySQLConnection object if the connection established successfully
#
# Use the cursor() method
# Use the cursor() method of a MySQLConnection object to create a cursor object to perform various SQL operations.
#
# Use the execute() method
# The execute() methods run the SQL query and return the result.
#
# Extract result using fetchall()
# Use cursor.fetchall() or fetchone() or fetchmany() to read query result.
#
# Close cursor and connection objects
# use cursor.clsoe() and connection.clsoe() method to close open connections after your work completes


# How to connect Mysql db Server
import mysql.connector


d1 = mysql.connector.connect(password='root',user='root',host='localhost')
print(d1)
# <mysql.connector.connection_cext.CMySQLConnection object at 0x0000027642F04820>


# CURD --> create, update,read,delete