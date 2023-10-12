import mysql.connector


db1 = mysql.connector.connect(password='root',host='localhost',user='root',database='meow')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()

# How to insert the values

insert = "insert into emp(sno,fname,lname,salary,location) values (%s,%s,%s,%s,%s)"

# %s:
# This part indicates that you're providing values to be inserted into the columns.
# The %s placeholders are used for string formatting and represent where actual values will be inserted.

# The %s placeholders are placeholders for values that you want to insert into the corresponding columns.
# The number of %s placeholders matches the number of columns specified in the column list.
# These placeholders are used to prevent SQL injection by properly escaping and formatting the values before they are inserted into the SQL query.

data = [(7,'venkata','laxmi',40000,'mumbai')]

db2.executemany(insert,data)

print(db2)

db1.commit()