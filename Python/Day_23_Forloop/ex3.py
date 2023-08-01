# how to excute the even numbers in new list

x1 = [22,77,89,13,15,55,91,32,84,42,25]
x2 = []
x3 = []
print('before x2:',x2)
for i in x1:
    if i%2==0:
        x2.append(i)
    else:
        x3.append(i)
print('After x2 even numbers:',x2)
# [22, 32, 84, 42]
print('odd numbers of x3',x3)

# After x2 even numbers: [22, 32, 84, 42]
# odd numbers of x3 [77, 89, 13, 15, 55, 91, 25]
