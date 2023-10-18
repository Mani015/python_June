
# The dir() function returns all properties and methods of the specified objects,
# without the values.This function will return all the properties and methods, even
# built in properties which are default for all objects


l1 = ['Ansuha','Jhansi','Laxmi']

# print(dir(l1))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


l1.append('priya')
print(l1)
# ['Ansuha', 'Jhansi', 'Laxmi', 'priya']
print(l1.__add__(['prasad','girish','sravani']))
#
# ['Ansuha', 'Jhansi', 'Laxmi', 'priya', 'prasad', 'girish', 'sravani']


l2 = [1,2]
l3 = l2.__doc__
print(l3)

# Built-in mutable sequence.
#
# If no argument is given, the constructor creates a new empty list.
# The argument must be an iterable if specified.