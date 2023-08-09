l1 = ['priya','laxmi','jhansi','anusha','sravani','prasad','girish']

# for i in range(len(l1)):
#     print(i,'index of ',l1[i])
# 0 index of  priya
# 1 index of  laxmi
# 2 index of  jhansi
# 3 index of  anusha
# 4 index of  sravani
# 5 index of  prasad
# 6 index of  girish


# enumerate
# The enumerate() function takes an iterable as its argument and returns an iterator that generates pairs of index and value tuples.
for i in list(enumerate(l1)):
    print(i)
# (0, 'priya')
# (1, 'laxmi')
# (2, 'jhansi')
# (3, 'anusha')
# (4, 'sravani')
# (5, 'prasad')
# (6, 'girish')

print()
fruits = ['apple', 'banana', 'orange', 'grape']
for index, fruit in enumerate(fruits):
    if index<1:
        continue
    print(f"Index {index}: {fruit}")
# Index 1: banana
# Index 2: orange
# Index 3: grape
