
# def Test1(x):
#     def Test2(y):
#         z = x + y
#         return z
#     print(Test2(5))
# Test1(10)
# 15

# def Test1(x):
#     def Test2(y):
#         z = x + y
#         print('local variable:',z)
#     return Test2(5)
#
# Test1(10)
# local variable: 15


def Test1(x):
    def Test2(y):
        z = x + y
        return z
    return Test2(5)
print(Test1(10))
# 15



