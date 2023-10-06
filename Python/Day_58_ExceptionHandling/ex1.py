
# What are Exceptions?
# An exception is an event that occurs during the execution of programs that disrupt the normal flow of execution
#  (e.g., KeyError Raised when a key is not found in a dictionary.) An exception is a Python object that represents an error..


# In Python, an exception is an object derives from the BaseException class that contains information about an error event that occurred within a method. Exception object contains:
#
# Error type (exception name)
# The state of the program when the error occurred
# An error message describes the error event.
# Exception are useful to indicate different types of possible failure condition.
#
# For example, bellow are the few standard exceptions
#
# FileNotFoundException
# ImportError
# RuntimeError
# NameError
# TypeError
#
#
# Why use Exception
# Standardized error handling: Using built-in exceptions or creating a custom exception with a more precise name and description, you can adequately define the error event, which helps you debug the error event.
#
# Cleaner code: Exceptions separate the error-handling code from regular code, which helps us to maintain large code easily.
#
# Robust application: With the help of exceptions, we can develop a solid application, which can handle error event efficiently
#
# Exceptions propagation: By default, the exception propagates the call stack if you don’t catch it. For example, if any error event occurred in a nested function,
# you do not have to explicitly catch-and-forward it; automatically, it gets forwarded to the calling function where you can handle it.
#
# Different error types: Either you can use built-in exception or create your custom exception and group them by their generalized parent class,
# or Differentiate errors by their actual class
#
# What are Errors?
# On the other hand, An error is an action that is incorrect or inaccurate. For example, syntax error. Due to which the program fails to execute.
#
# The errors can be broadly classified into two types:
#
# Syntax errors
# Logical errors
# Syntax error
# The syntax error occurs when we are not following the proper structure or syntax of the language. A syntax error is also known as a parsing error.
#
# When Python parses the program and finds an incorrect statement it is known as a syntax error. When the parser found a syntax error it exits with an error message without running anything.
#
# Common Python Syntax errors:
#
# Incorrect indentation
# Missing colon, comma, or brackets
# Putting keywords in the wrong place.

# Difference between Syntax Error and Exceptions
# Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.

# Exceptions: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))

c = a + b
print(c)

# Enter 1st number:3
# Enter 2nd number:4
# 7

print(a/b)
# ZeroDivisionError: division by zero







