
# \D	Returns a match where the string DOES NOT contain digits	"\D"

stu = 'Your good name is Darla, your telephone number : 023364653, your age is 12'

import re

st1 = re.findall('\D',stu)
print(st1)
# ['Y', 'o', 'u', 'r', ' ', 'g', 'o', 'o', 'd', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'D', 'a', 'r', 'l', 'a', ',', ' ', 'y', 'o', 'u', 'r', ' ', 't', 'e', 'l', 'e', 'p', 'h', 'o', 'n', 'e', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', ':', ' ', ',', ' ', 'y', 'o', 'u', 'r', ' ', 'a', 'g', 'e', ' ', 'i', 's', ' ']

# \s	Returns a match where the string contains a white space character

st2 = re.findall('\s',stu)
print(st2)
st3 = st2
print(st3.count(' '))
# 13


# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# print(sum(st2))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# \S	Returns a match where the string DOES NOT contain a white space character

st4 = re.findall('\S',stu)
print(st4)
# ['Y', 'o', 'u', 'r', 'g', 'o', 'o', 'd', 'n', 'a', 'm', 'e', 'i', 's', 'D', 'a', 'r', 'l', 'a', ',', 'y', 'o', 'u', 'r', 't', 'e', 'l', 'e', 'p', 'h', 'o', 'n', 'e', 'n', 'u', 'm', 'b', 'e', 'r', ':', '0', '2', '3', '3', '6', '4', '6', '5', '3', ',', 'y', 'o', 'u', 'r', 'a', 'g', 'e', 'i', 's', '1', '2']


# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string