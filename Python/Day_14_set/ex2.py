s1 = {}
# print(type(s1))
# <class 'dict'>
s2 = {1}
# print(type(s2))

# <class 'set'>


# set doesn't allows duplicate values


s3 = {1,2,3,4,'python','zomato',True,2}
# print(s3)

# {1, 2, 3, 4, 'zomato', 'python'}

# update()	Update the set with another set, or any other iterable
s4 = {'ysrparty'}
print(s4)
# syn: setname.update(value)
s4.update(s3)
print(s4)
# {1, 2, 3, 4, 'zomato', 'ysrparty', 'python'}
