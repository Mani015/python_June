
# Keyword Arguments in Python
# Functions can also be called using keyword arguments of the form kwarg=value.
#
# During a function call, values passed through arguments don’t need to be in the order
# of parameters in the function definition. This can be achieved by keyword arguments.
# But all the keyword arguments should match the parameters in the function definition.


def Display(a,b,c,d):
    print('a is :',a)
    print('b is :', b)
    print('c is :', c)
    print('d is :', d)
Display(a=1,b=2,c=3,d=4)
# a is : 1
# b is : 2
# c is : 3
# d is : 4