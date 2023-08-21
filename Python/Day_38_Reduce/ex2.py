# Reduce with lambda

from functools import reduce

print('sum of 1st 10 values:',reduce(lambda a, b : a+b, range(1,11)))
# sum of 1st 10 values: 55
print('subtraction of 1st 10 values:',reduce(lambda a, b : a-b, range(1,11)))
# subtraction of 1st 10 values: -53

# fiter with reduce(), lambda:

print(reduce(lambda x,y:x+y,filter(lambda x: x%4==0,range(1,100))))
# 1200

