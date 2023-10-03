
# sorted()

# print(help(sorted))
# Help on built-in function sorted in module builtins:
#
# sorted(iterable, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.
#
#     A custom key function can be supplied to customize the sort order, and the
#     reverse flag can be set to request the result in descending order.
#
# None

l1 = [22,45,46,2,10,20,55,99,95,87,13,34,38,42,12,-3,-4,-5,1,2]
print(l1)
print(sorted(l1))
# [-5, -4, -3, 1, 2, 2, 10, 12, 13, 20, 22, 34, 38, 42, 45, 46, 55, 87, 95, 99]
print(sorted(l1,reverse=True))
# Return a new list containing all items from the iterable in ascending order.
