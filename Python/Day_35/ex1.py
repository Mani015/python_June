l1 = []
for i in range(11): # Iterate loop
    if i%2==0: # Condition
        l1.append(i) # Expression
# print(l1)
# [0, 2, 4, 6, 8, 10]



l2 = []
for i in range(1,20):
    if i<11:
        l2.append(i)
# print(l2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#
# Example:

# List Comprehension
# syntax:[expression iterate condition]
# newlist = [expression for item in iterable if condition]

# if condition

# [expression for variable in iterable if condition]

x1 = [1,2,3,4,-5,6,-7,8,-2,4,-6,-32,7,8,9,3]

x2 = [i for i in x1 if i<0]
print(x2)
# [-5, -7, -2, -6, -32]


print([i for i in x1 if i>0])
# [1, 2, 3, 4, 6, 8, 4, 7, 8, 9, 3]

# Find out even numbers by using list comprehension
print([i for i in x1 if i%2==0])
# [2, 4, 6, 8, -2, 4, -6, -32, 8]

