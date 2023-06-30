x1 = 'python'
print(x1.lower())
# python
print(x1.islower())
# True

x2 = 'Python'
print(x2.islower())
# False

x3 = 'pythoN'
print(x3.islower())
# False


print(x3.isupper())
# False

x4 = 'PYTHON'
print(x4.isupper())
# True