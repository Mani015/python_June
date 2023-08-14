
g1 = 10
# print('g v:',g1)
def Outer():
    g1 = 20
    print('global v:',g1)  #global v: 20
    print('global v:',globals()['g1'])  #global v: 10
# Outer()


x1 = 100
def f1():
    x1 = 200
    print('Enclosig v:',x1)
    print('global v:',globals()['x1'])
    def f2():
        x1 = 300
        print('Local v:',x1)
        print('global v:', globals()['x1'])
        print('Enclosing v:',locals())

    f2()
f1()
# Enclosig v: 200
# global v: 100
# Local v: 300
# global v: 100
# Enclosing v: {'x1': 300}

