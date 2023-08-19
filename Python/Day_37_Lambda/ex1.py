
# Lambda functions are anonymous functions that can contain only one expression.

x = 10
# print(x)
# 10

# if x%2==0:
#     print(x,'even number')
# else:
#     print(x,'odd number')

# syntax:
# Lambda = (lambda arguments : expression)

l1 = (lambda x,y : x + y)
# print(l1)
# <function <lambda> at 0x000001754FC4DD30>

# print(l1(2,4))
# 6


# (lambda a,b: print(a*b))(2,6)
# 12


print((lambda x1,y1: x1//y1)(10,2)) # lambda is a single line fucntion
# 5

