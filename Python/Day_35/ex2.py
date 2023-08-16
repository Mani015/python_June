
# if else

# [expression  if condition else condition for i in iterable]

l1 = []
for i in range(1,11):
    if i%2==0:
        l1.append(i)
    else:
        l1.append(i+1)
# print(l1)
# [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]


# print([i if i%2==0 else i+1 for i in range(1,11)])
# [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]

# Remove the duplicate values
New = [i if i%2==0 else i+1 for i in range(1,11)]
print(set(New))
# {2, 4, 6, 8, 10}

x1 = range(1,11)
# print(x1)
# for i in x1:
#     print(i)
