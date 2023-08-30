
# Indirect calling

def f1():
    print('function1')
    f2()
def f2():
    print('fucntion2')
    f3()
def f3():
    print('fucntion3')
    f1()
# f3()
f1()
# function1

# fucntion2
# fucntion3


# RecursionError: maximum recursion depth exceeded while calling a Python object