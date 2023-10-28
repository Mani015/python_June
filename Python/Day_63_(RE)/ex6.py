# \w	Returns a match where the string contains any word characters (characters from

stu='you must be the change  you wish to see in the world'
import re
st1=re.findall('\w',stu)
print(st1)

# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
stu='you must be the change  you wish to see in the world'
import re
email='jhansirani.beeja@gmail.com$'
st2=re.findall('\W',email)
print(st2)
# ['y', 'o', 'u', 'm', 'u', 's', 't', 'b', 'e', 't', 'h', 'e', 'c', 'h', 'a', 'n', 'g', 'e', 'y', 'o', 'u', 'w', 'i', 's', 'h', 't', 'o', 's', 'e', 'e', 'i', 'n', 't', 'h', 'e', 'w', 'o', 'r', 'l', 'd']
# ['.', '@', '.', '$']
