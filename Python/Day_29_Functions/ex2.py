# A return statement is used to end the execution of the function call and “returns”
# the result (value of the expression following the return keyword) to the caller.
# The statements after the return statements are not executed.
# If the return statement is without any expression, then the special value None is returned.
# A return statement is overall used to invoke a function so that the passed statements can be executed.
# 3
# def Need(a,b):
#     c = a + b
#     print(c)
# print(Need(2,4))
# 6
# None

# using return keyword
def Need(a,b):
    c = a + b
    return c
# print(Need(2,4))
# 6



def Clever(x,y):
    z = x + y
    return z
print(Clever(3,6))
# 9
