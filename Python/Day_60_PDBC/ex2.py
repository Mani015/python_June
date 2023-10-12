# If you want to show the database in your mysql dbsever

import mysql.connector

db1 = mysql.connector.connect(password='root',host='localhost',user='root')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()

db2.execute('Show databases')

# print(db2)

for i in db2:
    print(i)

# ('cat',)
# ('chotu',)
# ('clincidb',)
# ('dairy',)
# ('emp',)
# ('information_schema',)
# ('jakir',)
# ('joins',)
# ('kit',)
# ('munna',)
# ('mysql',)
# ('naveenbro',)
# ('new',)
# ('patient',)
# ('performance_schema',)
# ('shop',)
# ('sridhar',)
# ('student',)
# ('sys',)

