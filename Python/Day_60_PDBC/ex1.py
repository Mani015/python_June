
# PDBC : Python database connection
# 1).mysql-connector
# 2).mysql-connector-python

import mysql.connector

db = mysql.connector.connect(password='root',host='localhost',user='root')

if db:
    print('connceted successfully')
else:
    print('connceted unsuccessfully')

print(db)
# connceted successfully
# <mysql.connector.connection_cext.CMySQLConnection object at 0x0000023FE3BD1A90>