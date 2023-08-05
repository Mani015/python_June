#
# x = [1,2,3,4,5,6,7]
# y = []
# for i in x:
#
#     if i & 2:
#         y.append(i)
# print(y)
# [2, 3, 6, 7]


x = [1,2,3,4,5,6,7]
y = []
for i in x:
    y.append(i & 2)
print(y)
# [0, 2, 2, 0, 0, 2, 2]
