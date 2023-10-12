
import mysql.connector


db1 = mysql.connector.connect(password='root',host='localhost',user='root',database='meow')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database
db2 = db1.cursor()

# db2.execute('select * from emp')
#
# for i in db2:
#     print(i)

    # (1, 'Sravani', 'priya', 40000, 'Banglore')
    # (2, 'Jhansi', 'Rani', 30000, 'Hyderabad')
    # (3, 'Padma', 'priya', 50000, 'kadapa')
    # (4, 'prasad', 'prasad', 40000, 'chennai')
    # (5, 'Girish', 'kumar', 30000, 'Tirupati')
    # (6, 'Anusha', 'Tellakula', 50000, 'vizag')
    # (7, 'venkata', 'laxmi', 40000, 'mumbai')

# limit data

# db2.execute('select * from emp limit 4')
# for i in db2:
#     print(i)

# (1, 'Sravani', 'priya', 40000, 'Banglore')
# (2, 'Jhansi', 'Rani', 30000, 'Hyderabad')
# (3, 'Padma', 'priya', 50000, 'kadapa')
# (4, 'prasad', 'prasad', 40000, 'chennai')


# Specified columns


db2.execute('select fname,lname,salary from emp')
for i in db2:
    print(i)

# ('Sravani', 'priya', 40000)
# ('Jhansi', 'Rani', 30000)
# ('Padma', 'priya', 50000)
# ('prasad', 'prasad', 40000)
# ('Girish', 'kumar', 30000)
# ('Anusha', 'Tellakula', 50000)
# ('venkata', 'laxmi', 40000)
