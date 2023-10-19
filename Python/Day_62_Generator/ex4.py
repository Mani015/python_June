
# Iterate the sequence of values by using for loop

l1 = range(1,11)

New1 = map(lambda x:x**2,l1)
print(next(New1))
#
print(next(New1))
# 4
print('for loop iterate next value ')

for i in New1:
    print(i)

# 1
# 4
# for loop iterate next value
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
