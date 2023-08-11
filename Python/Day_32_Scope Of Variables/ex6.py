
g1 = 10
print('global variable:',g1)
def outer():
    print('global variable:', g1)
    def inner():
        l1 = 30
        print('local variable:',l1)
        print('global variable:',g1)
    inner()
    print('global variable:',g1)
outer()
print('global variable:',g1)
# global variable: 10
# global variable: 10
# local variable: 30
# global variable: 10
# global variable: 10
# global variable: 10