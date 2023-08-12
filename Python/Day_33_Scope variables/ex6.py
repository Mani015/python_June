
# Adding the global and local variable (same name of both)
# To get the out side of the fucntion

Var1 = 10
print('global variable:',Var1)
def Sum():
    Var1 = 15
    print('local variable:',Var1)
    print('global variable: ',globals()['Var1'])
    Adding = Var1 + globals()['Var1']
    return Adding
var2  = Sum()
print('variable of Var2:',var2)
# global variable: 10
# local variable: 15
# global variable:  10
# variable of Var2: 25
