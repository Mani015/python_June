
t1 = (45,46,2,10,20,55,99,95,87,13,34,38,10)

# print(sorted(t1))
# [2, 10, 10, 13, 20, 34, 38, 45, 46, 55, 87, 95, 99]

# print(sorted(t1,reverse=True))
# [99, 95, 87, 55, 46, 45, 38, 34, 20, 13, 10, 10, 2]

d1 = {2:'s',9:'r',6:'r',21:'w',7:'c',4:'q'}

print(d1)

print(sorted(d1))
# [2, 4, 6, 7, 9, 21]

# You want to get ascending order
v1 = d1.values()
print(v1)
# dict_values(['s', 'r', 'r', 'w', 'c', 'q'])
print(sorted(v1))
# ['c', 'q', 'r', 'r', 's', 'w']

print(sorted(d1.items()))
# [(2, 's'), (4, 'q'), (6, 'r'), (7, 'c'), (9, 'r'), (21, 'w')]

print(sorted(d1.items(),key=lambda val:val[1]))
# [(7, 'c'), (4, 'q'), (9, 'r'), (6, 'r'), (2, 's'), (21, 'w')]


x1 = [1,2,1,3,5,6,78,7,65,4,32,2,4,56,7,8,9,8,75,3,2,2,2,2,22,3,45,5,6,77,8,9]
# {2:__,1:__}
