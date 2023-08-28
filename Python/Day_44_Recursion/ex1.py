# RECURSION:
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.
def fun():
    print('hello function')
    fun() # Function calling it self
fun()

# hello function
# hello function
# hello function
# hello function
# hello function
# Traceback (most recent call last):
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_44_Recursion\ex1.py", line 9, in <module>
#     fun()
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_44_Recursion\ex1.py", line 8, in fun
#     fun()
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_44_Recursion\ex1.py", line 8, in fun
#     fun()
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_44_Recursion\ex1.py", line 8, in fun
#     fun()
#   [Previous line repeated 993 more times]
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_44_Recursion\ex1.py", line 7, in fun
#     print('hello function')
# RecursionError: maximum recursion depth exceeded while calling a Python object



