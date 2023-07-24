
# setdefault()	Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value
d1 = {1:'int'}
print(d1)
# {1: 'int'}
d1.setdefault(234,'int')
print(d1)
# {1: 'int', 234: 'int'}
# d1.setdefault([5,6,7,8,9],'int')
# print(d1)
# TypeError: unhashable type: 'list'

d1.setdefault(567)
print(d1)
# {1: 'int', 234: 'int', 567: None}

d1.setdefault(4,'four')
print(d1)
# {1: 'int', 234: 'int', 567: None, 4: 'four'}
# d1.setdefault(,'hello')
# print(d1)
d1[567]='unick number'
print(d1)
# {1: 'int', 234: 'int', 567: 'unick number', 4: 'four'}

v1 = 'hello'
d1[v1] = d1.pop(567)
print(d1)

# d1.setdefault(v1,'girish')
# print(d1)

