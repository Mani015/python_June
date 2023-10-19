
def Fun():
    return 10

# x1 = Fun()
# print(type(Fun))
# <class 'function'>

# GENERATOR:Python provides a generator to create your own iterator function.
# A generator is a special type of function which does not return a single value,
# instead, it returns an iterator object with a sequence of values.
# In a generator function, a yield statement is used rather than a return statement.
# The following is a simple generator function.
def Fun2():
    yield 10

# x2 = Fun2()
# print(type(Fun2()))
# <class 'generator'>


