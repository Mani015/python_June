
import module1
# Approaching_1
print(module1.Addition(12,13))
# 25

print(module1.Subtraction(3,2))
# 0
print(module1)
# <module 'module1' from 'C:\\Users\\Test\\PycharmProjects\\pythonProject\\Day_39-Modulus\\module1.py'>
print(type(module1))
# <class 'module'>


import sys
print('Size Taken:',sys.getsizeof(module1))
# Size Taken: 72
print(id(module1))
# 2700051808320