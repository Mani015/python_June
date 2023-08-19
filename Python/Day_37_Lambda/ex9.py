

# map with filter

# filter:
print(list(filter(lambda x: x%1==0,range(1,21))))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list(map(lambda i:i*2,filter(lambda x: x%1==0,range(1,21)))))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]


# filter with map

print(tuple(filter(lambda i:i>21,map(lambda x : x*2,range(1,21)))))
# (22, 24, 26, 28, 30, 32, 34, 36, 38, 40)
