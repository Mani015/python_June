
# map(), filter(), and reduce() are three built-in functions in Python that are often used in functional programming paradigms
# for processing and transforming data. They are part of the functools module in Python 3, and prior to Python 3, reduce() was a built-in function in the functools module as well.



# map() Function:
# The map() function applies a given function to all items in an iterable and returns an iterator containing the results.
# Syntax: map(function, iterable)

l1 = [1,2,3,4,5,6,7,8,9,10]
# for i in l1:
    # print(list(i*i))
# TypeError: 'int' object is not iterable
# iterables: list,tuple,set,dict

def Square(num):
    return num**2

l2 = [1,2,3,4,5,6,7,8,9,0]

M1 = tuple(map(Square,l2))
# print(type(M1))
# <class 'map'>
print(M1)
# <map object at 0x000002CCDD0C1280>

# (1, 4, 9, 16, 25, 36, 49, 64, 81, 0)



