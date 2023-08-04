l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [] # Taking another list

# using for loop because each value Iterate
for i in l1:
    l2.append(i+1)
# print(l2)

#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# using break keyword
l3 = [] # New list
for i in range(0,11):
    if i==7:
        break
    l3.append(i+1)
print(l3)
# [2, 3, 4, 5, 6, 7]


