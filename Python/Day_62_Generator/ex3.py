
# We have taken one list

l1 = [1,2,3,4,5,6,7,8,9,10]

New = map(lambda x: x**2,l1)
print(New)
# <map object at 0x000002940E8C0BB0>
# print(list(New))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(set(New))

# We have to produce sequence of values

print(next(New))
# 1
print(next(New))
# 4

print(next(New))
# 9

print(next(New))
print(next(New))
print(next(New))
print(next(New))
print(next(New))
print(next(New))
# 16
# 25
# 36
# 49
# 64
# 81
print(next(New))
# 100
print(next(New))
# StopIteration
