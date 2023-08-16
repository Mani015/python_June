
# How to remove duplicate values

l1 = [1,2,3,4,5,6,7,8,1,2,3,7,5,64,43,2,88,99,100]

l2 = [] # Take one Empty list
# Iterate the l1 using for loop
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        print(i,end=' ')
        print()
# 1 2 3 7 5 2
print(l2)
# [1, 2, 3, 4, 5, 6, 7, 8, 64, 43, 88, 99, 100]
