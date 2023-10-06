# SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
# TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
# NameError: This exception is raised when a variable or function name is not found in the current scope.
# IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
# KeyError: This exception is raised when a key is not found in a dictionary.
# ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
# AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
# IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
# ImportError: This exception is raised when an import statement fails to find or load a module.

l2 = [11,22,33,44,55]
print(l2)
a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))
# Try and Except Statement – Catching Exceptions
# Try and except statements are used to catch and handle exceptions in Python.
# Statements that can raise exceptions are kept inside the try clause and the statements
# that handle the exception are written inside except clause.
try:
  print(a/b)
except:
    print('Error occured')
for i in range(5):
    print('😁😁😁')

# [11, 22, 33, 44, 55]
# Enter 1st number:4
# Enter 2nd number:2
# 2.0
# 😁😁😁
# 😁😁😁
# 😁😁😁
# 😁😁😁
# 😁😁😁
