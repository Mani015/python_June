

l1 = [1,2,3,4,5,6,7,8]
# print(sum(l1))
l2 = [8,7,6,5,4,3,2,1]
l3 = []
for i,j in zip(l1,l2):
    l3.append(i+j)
# print(l3)
# [9, 9, 9, 9, 9, 9, 9, 9]


# sum the 1st 10 values using for loop

sum = 0
print('sum value :',sum)
# sum value : 0

for i in range(1,11):
    sum+=i  # sum = sum + i
print('After for loop:',sum)
# After for loop: 55



