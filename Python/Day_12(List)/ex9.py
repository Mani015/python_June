# adding two list

l1 = [1,2,3,4,5,6,7,13+10j,22+8j,7.8]
l2 = [11,22,33,44,55,66,1+2j,5+7j,5.3]
print(l1+l2)

# [1, 2, 3, 4, 5, 6, 7, (13+10j), (22+8j), 7.8, 11, 22, 33, 44, 55, 66, (1+2j), (5+7j), 5.3]

# print(l1-l2)
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

# Repeation of list

print([1,2,3]*2)
# [1, 2, 3, 1, 2, 3]

print([1,2,3,4]**2)
# TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
