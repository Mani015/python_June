# Frozenset

s1 = {1,2,3,4,5,6,7}
# print(s1[1])
print(type(s1))
# <class 'set'>


s2 = frozenset(s1)
print(s2)
print(type(s2))
# frozenset({1, 2, 3, 4, 5, 6, 7})
# <class 'frozenset'>


l1 = ['happy','sad','lonely','weird','padma priya','priya padma']

fz1 = frozenset(l1)
print(type(fz1))
print(fz1)

# <class 'frozenset'>
# frozenset({'sad', 'happy', 'padma priya', 'weird', 'lonely', 'priya padma'})
