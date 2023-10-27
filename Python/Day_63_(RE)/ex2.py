
# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
#
# If there is more than one match, only the first occurrence of the match will be returned:


s1 = 'Theexpert in anything was a once a beginner'

import re

x1 = re.search('expert',s1)
print(x1)
print(x1.group())
# <re.Match object; span=(4, 10), match='expert'>
# expert


x2 = re.search('The',s1)
print(x2)
# <re.Match object; span=(0, 3), match='The'>


x3 = re.search('Jhansi',s1)
print(x3)
# None



txt = "The rain in Spain"
x = re.search("\s", s1)

print("The first white-space character is located in position:", x.start())
# The first white-space character is located in position: 3