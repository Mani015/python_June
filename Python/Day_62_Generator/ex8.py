
l1 = map(lambda x: x**2,range(1,11))
# print(list(l1))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('__next__()')
print(l1.__next__())
# 1
print(l1.__next__()) # 4
print(l1.__next__()) # 9
print(l1.__next__()) #16
print(l1.__next__()) # 25
print('next()')
print(next(l1))
# 36
print(next(l1)) # 49
print('For loop')
for i in l1:
    print(i)


# __next__()
# 1
# 4
# 9
# 16
# 25
# next()
# 36
# 49
# For loop
# 64
# 81
# 100


