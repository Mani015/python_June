# Type conversion/Casting:


a1 = 14
print(type(a1))
# <class 'int'>

# int to float

a2 = float(a1)
print(type(a2))
print('float of :',a2)
# <class 'float'>
# float of : 14.0

# float to complex

a4 = complex(a2)
print(type(a4))
print(a4)
# <class 'complex'>
# (14+0j)


a3 = bool(a4)
print(a3)
print(type(a3))
# True
# <class 'bool'>
