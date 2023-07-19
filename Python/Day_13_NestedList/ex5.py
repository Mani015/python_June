
# A tuple is a collection which is ordered and unchangeable.

t3 = ('cherry','jerry','tom','berry','chotabeam','calf','nephew','tom')
print(t3)

print(t3.index('tom'))
# 2
print(t3[2])
# tom

print(t3.index('tom',3,10))
# 7


print(t3.count('berry'))
# 1

print(t3.count('tom'))
# 2
# print(t3.count('tom',3))
# TypeError: tuple.count() takes exactly one argument (2 given)

t4 = (1,2,3,4,5,(2,3,4,5,6),3,4,5,6)
print(t4)


# examplexs: adhar card no, voter id, vechile number, pancard,ration card,fingerprint,
