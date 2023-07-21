
# discard()	Remove the specified item
s1 = {'pavan','vinod','kumar','prasad','girish','cnu','deepika','gowthami'}

print(s1)
# syn:set.discard(value)
print()
s1.discard('cnu')
print(s1)
# {'vinod', 'prasad', 'gowthami', 'girish', 'pavan', 'deepika', 'kumar'}

s1.discard('bharath')
print(s1)

s1.remove('bharath')
print(s1)
# KeyError: 'bharath'

