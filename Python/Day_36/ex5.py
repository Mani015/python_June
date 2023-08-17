price = 10000
print('Global variable:',price)

def Samsung():
    global price
    price = 12000
    print('local variable:',price)
    print('global var:',globals()['price'])

Samsung()

# Global variable: 10000
# local variable: 12000
# global var: 12000

# In this example, without the global keyword inside the modify_global function, the code would create a new local
