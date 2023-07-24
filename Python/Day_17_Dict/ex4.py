
dc1 = {'name':'jhnasi','domain':'Python Fullstack','salary':50000,'id':560037}
print(dc1)
# {'name': 'jhnasi', 'domain': 'Python Fullstack', 'salary': 50000, 'id': 560037}
emp_Id = 'Employee_ID'

dc1[emp_Id] = dc1.pop('id')
print(dc1)
# {'name': 'jhnasi', 'domain': 'Python Fullstack', 'salary': 50000, 'Employee_ID': 560037}

dc1['salary'] = 70000
print(dc1)

# {'name': 'jhnasi', 'domain': 'Python Fullstack', 'salary': 70000, 'Employee_ID': 560037}

# popitem()	Removes the last inserted key-value pair
# dc1.popitem('name')
# print(dc1)
# TypeError: dict.popitem() takes no arguments (1 given)

dc1.popitem()
print(dc1)
# {'name': 'jhnasi', 'domain': 'Python Fullstack', 'salary': 70000}
dc1.popitem()
print(dc1)
# {'name': 'jhnasi', 'domain': 'Python Fullstack'}
