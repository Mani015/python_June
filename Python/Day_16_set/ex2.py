
# symmetric_difference()	Returns a set with the symmetric differences of two sets
s1 = {1,2,3,4,5,6}
s2 = {2,3,4,5,6,7,8,9,0,10}

# print(s1.symmetric_difference(s2))

# {0, 1, 7, 8, 9, 10}
# print(s2.symmetric_difference(s1))
# {0, 1, 7, 8, 9, 10}



# s3 = frozenset(s1)

x1 = {'sunday','monday','satuarday'}
x2 = {'Tuesday','friday','thursady','sunday'}

print(x1.symmetric_difference(x2))
# {'friday', 'thursady', 'monday', 'satuarday', 'Tuesday'}
