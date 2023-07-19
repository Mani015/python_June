
# Nested List:

# The easiest way to create a nested list in Python is
# simply to create a list and put one or more lists in that list.

l1 = [1,2,3,4,5,[1,2,3,4],6,7,[11,22,33],8,[12,13,14],9,10]

print(l1)
# [1, 2, 3, 4, 5, [1, 2, 3, 4], 6, 7, [11, 22, 33], 8, [12, 13, 14], 9, 10]
print(l1[0])
# 1
print(l1[1])
# 2
print(l1[2])
# 3
print(l1[3])
# 4
print(l1[4])
# 5
print(l1[5])
# [1, 2, 3, 4]
print(l1[6])
# 6
print(l1[7])
# 7
print(l1[8])
# [11, 22, 33]


