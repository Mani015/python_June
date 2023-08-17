# The nonlocal keyword is used in programming languages like Python to indicate
# that a variable being modified or accessed within a nested function
# is not local to that function but belongs to an enclosing (outer) function's scope.
# This is relevant when dealing with nested functions,
# such as when you have a function defined within another function.

g1 = 10
print('global var:',g1) #10
def Outer():

    g2 = 20
    print('Enclosing var:',g2)#20
    print('global var:', g1)#10
    def Inner():
        nonlocal g2
        g2 = 30
        print('local vari:',g2)#30
        print('global var:', g1)#10
    print('Enclosing var:', g2) #20
    Inner()
    print('Enclosing var:', g2)# 30
Outer()
# global var: 10
# Enclosing var: 20
# global var: 10
# Enclosing var: 20
# local vari: 30
# global var: 10
# Enclosing var: 30