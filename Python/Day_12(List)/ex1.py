
l1 = [1,2,3,'pavan','vinay','Raju',12.0,23+4j,True]

print(l1)
# [1, 2, 3, 'pavan', 'vinay', 'Raju', 12.0, (23+4j), True]

# append():takes exactly one arguments, adding the current end of the list

# syntax: list.append(element)
l1.append("can't")
print(l1)
# [1, 2, 3, 'pavan', 'vinay', 'Raju', 12.0, (23+4j), True, "can't"]

l1.append('prasad')
print(l1)
# [1, 2, 3, 'pavan', 'vinay', 'Raju', 12.0, (23+4j), True, "can't", 'prasad']

l1.append(2)
print(l1)
# [1, 2, 3, 'pavan', 'vinay', 'Raju', 12.0, (23+4j), True, "can't", 'prasad', 2]


l1.append('Girish',"subba Raju")
print(l1)

# TypeError: list.append() takes exactly one argument (2 given)

