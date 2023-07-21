
# difference_update()	Removes the items in this set that are also included in another, specified set


a1 = {'a','b','c','d','e'}
# print('before a1:',a1)
# before a1: {'d', 'a', 'c', 'b', 'e'}
a2 = {'g','h','i','j','l','a','d'}
print('before a2:',a2)
# before a2: {'g', 'i', 'j', 'a', 'd', 'l', 'h'}

# a1.difference_update(a2)
# print('after a1:',a1)
# after a1: {'b', 'c', 'e'}


a2.difference_update(a1)
print('after a2:',a2)
# after a2: {'h', 'l', 'j', 'i', 'g'}
