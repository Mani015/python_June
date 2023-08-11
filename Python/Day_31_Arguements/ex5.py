# How FInd out Duplicate values in list:

l1 = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,6,8,9,11,22,33]
l2 = [1,2,3,4,5,6,7,8,9,0,]

for i in l1:
    if i not in l2:
        l2.append(i)
    # else:
    #     print(i,end=' ')
# 1 2 3 4 6 8 9
print(l2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22, 33]
