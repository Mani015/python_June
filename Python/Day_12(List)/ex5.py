
# pop()	Removes the element at the specified position

x2 = [1,2,3,4,5,6,7,8,9,10]
print(x2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we Don't give with out specified position (by defaultly takes end of the value)
# syn: list.pop()

x2.pop()
print(x2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
x2.pop()
print(x2)
# [1, 2, 3, 4, 5, 6, 7, 8]

# with specified position

x2.pop(3)
print(x2)
# [1, 2, 3, 5, 6, 7, 8]

x2.pop(6)
print(x2)
# [1, 2, 3, 5, 6, 7]

x2.pop(6)
print(x2)
# IndexError: pop index out of range
