# update()	Updates the dictionary with the specified key-value pairs
# syn:dictionar.update({key:value})

d1 = {'name':'balaraju','age':19,'Gender':'Male','height':5.8}
print(d1)
# {'name': 'balaraju', 'age': 19, 'Gender': 'Male', 'height': 5.8}
d1.update({'mobile':1234567891})
# print(d1)
# {'name': 'balaraju', 'age': 19, 'Gender': 'Male', 'height': 5.8, 'mobile': 1234567891}

d1.update({'email':'balaraju@gmail.com',"weight":100})
# print(d1)
# {'name': 'balaraju', 'age': 19, 'Gender': 'Male', 'height': 5.8, 'mobile': 1234567891, 'email': 'balaraju@gmail.com', 'weight': 100}

d1['name'] = 'B/Subbaraju'
print(d1)
# {'name': 'B/Subbaraju', 'age': 19, 'Gender': 'Male', 'height': 5.8, 'mobile': 1234567891, 'email': 'balaraju@gmail.com', 'weight': 100}

d1['age'] = 25
print(d1)
# {'name': 'B/Subbaraju', 'age': 25, 'Gender': 'Male', 'height': 5.8, 'mobile': 1234567891, 'email': 'balaraju@gmail.com', 'weight': 100}

# updating the key name
new_number = 'Contact'
d1[new_number] = d1.pop('mobile')
print(d1)
# {'name': 'B/Subbaraju', 'age': 25, 'Gender': 'Male', 'height': 5.8, 'email': 'balaraju@gmail.com', 'weight': 100, 'Contact': 1234567891}


