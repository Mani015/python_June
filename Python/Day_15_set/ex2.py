
# union()	Return a set containing the union of sets


s1 = {1,2,3,4,5,6,7}
s2 = {1,2,8,9,10}
# syn: s1.union(s2)

print(s1.union(s2))
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


s3 = {'django','mysql','flask'}

print(s3.union(s1))
# {1, 2, 3, 4, 5, 6, 7, 'flask', 'mysql', 'django'}


