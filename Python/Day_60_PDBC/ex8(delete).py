

# delete the data particular row

import mysql.connector
db1 = mysql.connector.connect(password='root',host='localhost',user='root',database='meow')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()


delete = "delete from emp where fname='Girish'"

db2.execute(delete)
print(db2)

db1.commit()