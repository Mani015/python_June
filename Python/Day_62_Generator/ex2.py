
x1 = range(1,11)
print(x1)

import sys

print('range size taken:',sys.getsizeof(x1))
# range size taken: 48

print('range fucntion passes in side of list:',sys.getsizeof(list(x1)))
# range fucntion passes in side of list: 136

name = 'priya'

for i in x1:
    print(sys.getsizeof(name),sys.getsizeof(i))
