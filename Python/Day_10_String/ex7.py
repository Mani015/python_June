
st1 = "eat run sleep repeat work"
# syn: stringName.split('value',maxsplit)
print(st1.split('a'))
# ['e', 't run sleep repe', 't work']

st2 = "java programming python programming c programming c++ programming"

# print(st2.split('programming'))
# ['java ', ' python ', ' c ', ' c++ ', '']


print(st2.split('programming',2))
# ['java ', ' python ', ' c programming c++ programming']


x1 = "11261050"
print(x1.split('1',1))
# ['', '', '26', '050']


