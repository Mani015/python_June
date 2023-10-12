import mysql.connector
db1 = mysql.connector.connect(password='root',host='localhost',user='root',database='meow')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()

# update the data from table
update = "update emp set location='vijayawada' where sno=6"

db2.execute(update)
print(db2)

db1.commit()
