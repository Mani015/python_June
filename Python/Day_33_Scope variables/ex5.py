# How TO access the global varaible inside the function with same name of local variable

# global and local variables are same but different values


# x1 = 10
# print('x1 is global v:',x1)
# def Same():
#     x1 = 20
#     print('local variable:',x1)
#     print('global variable:',x1)
# Same()

# x1 is global v: 10
# local variable: 20
# global variable: 20

# TO get(global variable) the same variable name of global and locals using the globals() method

x1 = 10
print('x1 is global v:',x1)
def Same():
    x1 = 20
    print('local variable:',x1)
    print('global variable:',globals()['x1'])   # Here using globals() method
Same()
# x1 is global v: 10
# local variable: 20
# global variable: 10



