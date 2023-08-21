from functools import reduce
# syn: reduce(functionname,iterable)
# def Remark(x,y):
#     return x+y
#
# t1 = (2,4,5,7,3,1,2,3,5,6)
#
# R1 = reduce(Remark,t1)
# print(R1)
# # 38


def Remark(x,y):
    return x*y

t1 = (2,4,5,7,3,1,2,3,5,6)

R1 = reduce(Remark,t1)
print(R1)
# 151200