# Regular expressions (regex) are patterns used to match and manipulate strings of text.
# They are widely used in programming and text processing to search, match, and manipulate text based on specific patterns.
#
# Here are some common components and syntax used in regular expressions:
#
# Literal Characters: Ordinary characters like letters, digits, and symbols represent themselves. For example, the regex pattern "cat" matches the string "cat" exactly.
#
# Metacharacters: These are special characters with reserved meanings in regex. Some common metacharacters include:

# syntax: re.functionname(pattren,string,flags=0)
# match,search,findall,finditer,split,sub
#


# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.

simple_Fact = 'If you do not work with Interest and attention ,No matter what you do,you will waste of your time'

# Match Object
# A Match Object is an object containing information about the search and the result.

import re as R
m1 = R.match('If',simple_Fact)
print(m1)
# <re.Match object; span=(0, 2), match='If'>
print(m1.group())
# If

m2 = R.match('Interest',simple_Fact)
print(m2)
print(m2.group())
# None
# AttributeError: 'NoneType' object has no attribute 'group'
