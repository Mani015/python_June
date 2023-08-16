
l1 = ['priya','jhansi','prasad','girish']

l2 = [i.upper() for i in l1]
# print(l2)

l3 = []
l4 = [l3.append(i) for i in l1]
# print(l4)
# [None, None, None, None]

x1 = [l3.append(i**2) for i in range(1,11)]
# print(x1)
# print(l3)







name = ['priya','prasad','jhansi','girish','laxmi','sravani']

names2 = ['anusha','stella']

z1 = [name.append(i) for i in names2]
print(name)
# ['priya', 'prasad', 'jhansi', 'girish', 'laxmi', 'sravani', 'anusha', 'stella']
print(z1)













