# Decorators
'''A higerorder function is a function that operates on other function,
either as its argument or by returning a function.'''

'''Decorators are higher order functions because they take in a function and return a 
function'''

# With out decorator
# def Outer(func):
#     def Inner():
#         result = func
#         return 'Hello, Good evening', result
#     return Inner()
#
# def new():
#     return 'Jhansi'
#
#
# print(Outer(new()))
# ('Hello, Good evening', 'Jhansi')



def Outer(func):
    def Inner():
        result = func()
        return 'Hello, Good evening', result
    return Inner

def new():
    return 'Jhansi'
# print(Outer(new()))
# <function Outer.<locals>.Inner at 0x000002897F673310>

# var = Outer(new)
# print(var())




# With decorator

def Outer1(func):
    def Inner():
        result = func()
        return 'Hello, Good evening', result
    return Inner

@Outer
def new1():
    return 'Padma priya'

print(new1())
# ('Hello, Good evening', 'Padma priya')









