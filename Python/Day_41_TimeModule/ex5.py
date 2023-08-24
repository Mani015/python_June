import datetime

d = datetime.datetime.today()
print(d.day, d.month, d.year)
print(d.second, d.microsecond, d.minute)
print(d.__class__)
print(type(d))
# 24 8 2023
# 23 984449 14
# <class 'datetime.datetime'>
# <class 'datetime.datetime'>
