
fruits = ['apple','mango','graphes','pineapple','orange','pappaya','banana']

price = [270,100,100,70,250,60,20]

# if you want to pair both list values using zip()

print(list(zip(fruits,price)))

# [('apple', 270), ('mango', 100), ('graphes', 100), ('pineapple', 70), ('orange', 250), ('pappaya', 60), ('banana', 20)]


print(id(fruits))
# 1830525025344

import sys
print(sys.getsizeof(fruits))
# 120

