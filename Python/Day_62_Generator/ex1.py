
# In python , a Generators is a fucntion that returns an iterator that produces a sequence of
# values when Iterated over

#  Generator are usefull when we want to produce a large sequence of values,
# but we don't want to store all of them in memory at once.

l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
print(id(l1))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1838980479872
# We are trying to know the size of this list

import sys

print('list size taken:',sys.getsizeof(l1))
# list size taken: 152

t1 = (1,2,3,4,5,6,7,8,9,10)
print('tuple taken:',sys.getsizeof(t1))
# tuple taken: 120
list_size = sys.getsizeof(l1)
tuple_size = sys.getsizeof(t1)

final_difference = list_size - tuple_size
print('Overall difference:', final_difference)
# Overall difference: 32
