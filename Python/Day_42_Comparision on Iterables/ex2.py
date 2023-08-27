
# COMPARISION ON ITERABLES
print([1,2]>[2,1])
# False
#

# same value in both list it will returns no result,
# Go to next value
print([1,2]>[1,3])
# False

print([1,2,3]>[1,2,3])
# 1>1-->NO RESULT ,GO TO NEXT VALUE
# 2>2-->NO RESULT ,GO TO NEXT VALUE
# 3>3-->NO RESULT ,GO TO NEXT VALUE
# It will takes both lists length ---> same lenght it will return false


print([1,2,3]>[2,3,1])
# False

print([2,1,3,4,5,6]>[3,4,5,1,2,3])
# False

print([2,1,3,4,1,3,2]>[1,2,3,1,2,3])
# True

print([3,4,1,2,3]>[-3,1,3,24])
# True

print([-1,-2,-3]>[-3,-2,-1])
# True