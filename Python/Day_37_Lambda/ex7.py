
# filter() Function:
# The filter() function applies a given function to all items in an iterable and returns
# an iterator containing only the items that satisfy a certain condition.
# Syntax: filter(function, iterable)


x1 = [7,9,48,72,68,86,37,53]



def Even_Function(even):
    if even%2==0:
        return even
f1 = filter(Even_Function,x1)
# print(type(f1))
# <class 'filter'>

# print(tuple(f1))
# (48, 72, 68, 86)


# Using lambda

print(list(filter(lambda x1 : x1%2==0,x1)))

# [48, 72, 68, 86]
