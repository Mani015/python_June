
# Global Variable in function
# A Global variable is a variable that declares outside of the function.
# The scope of a global variable is broad.
# It is accessible in all functions of the same module.

Global_var = 10

def Global_Func():
    print('I am function') #I am function
    print('Global var:',Global_var) # global variable is accessing the inside of function
    #I am function
    #Global var: 10

Global_Func()
print('global variable:',Global_var)
# I am function
# Global var: 10
# global variable: 10


