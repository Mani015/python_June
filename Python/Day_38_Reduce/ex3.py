from functools import reduce
# print(filter(lambda x:'even number' if x%2==0 else 'odd number',reduce(lambda i,j: i + j,[1,2,3,4,5])))

x = reduce(lambda x,y : x+y,range(-10,0))
print(x)
# -55

# print(list(filter(lambda x : x%2==0 ,list(x))))

for i in x:
    print(i)
# TypeError: 'int' object is not iterable

