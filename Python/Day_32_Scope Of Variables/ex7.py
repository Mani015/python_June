g1 = 10
print('global variable:',g1)
def outer():
    En_var = 20 # Non-local variable
    print('global variable:', g1)
    print('Enclosing variable:',En_var)
    def inner():
        l1 = 30  #Local variale
        print('local variable:',l1)
        print('global variable:',g1)
    inner()
    print('global varia ble:',g1)
outer()
print('global variable:',g1)