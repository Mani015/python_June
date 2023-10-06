
l1 = [11,22,33,44,55]
print(l1)
# IndexError: list index out of range

try:
    print(l1[5])
except ZeroDivisionError as Zero:
    print(Zero,'Error occured')
except IndexError as Index:
    print(Index,'Error occured')
except ValueError as Value:
    print(Value,'Error Occured')

def function(a):
    return a+30

x1 = function(20)
print(x1)

# [11, 22, 33, 44, 55]
# list index out of range Error occured
# 50
