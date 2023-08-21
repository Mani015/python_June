
# map,filter,with reduce

from functools import reduce

print(reduce(lambda a,b: a+b,filter(lambda x: x%2==1,map(lambda y:y*y,range(1,11)))))

l1 = []
for i in range(1,11):
    if i%2==1:
        l1.append(i**2)
print('sum of odd numbers:',sum(l1))
# 165
# sum of odd numbers: 165

