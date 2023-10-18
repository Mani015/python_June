
# 2). Passing Function as an Argument in Python

def Square(var):
    return var**2
def Cube(var):
    return var**3

def Changemethod(fun):
    print(fun(5))
Changemethod(Cube)
Changemethod(Square)
# 125

# 25