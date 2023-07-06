
x1 = 'Subba Raju'

x2 = 'Nithin'

x3 = 'Alex'

print(x1 is not x3)
# True
print(x2 is not x2)
# False

print(not(x3 is not x3))
# True
x4 = x1

print(x1 is not x5)
# NameError: name 'x5' is not defined
