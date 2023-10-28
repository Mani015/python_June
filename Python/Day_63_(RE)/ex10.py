
name = 'python'
for i in range(len(name)):
    print(i,'index of:',name[i])

print()

import re

# find iter value index

st3 = 'I will fight for the right'



for i in re.finditer('i',st3):
    t1 = i.span()
    print(t1)
# (3, 4)
# (8, 9)
# (22, 23)

