
# \A	Returns a match if the specified characters are at the beginning of the string

s1 = "Believe you can and you are halfway there  do anything"
import re
a1 = re.findall('\ABelieve',s1)
print(a1)
# ['Believe']
a2 = re.findall('\Ayou',s1)
print(a2)
# []


# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")

b1 = re.findall(r'Believe\b',s1)
print(b1)
# ['Believe']

b2 = re.findall(r'anything\b',s1)
print(b2)

# ['anything']

b3 = re.findall(r'prasad\b',s1)
print(b3)
# []

# \d	Returns a match where the string contains digits (numbers from 0-9)

data = 'My name is Jhansi ,cellno 74358797538469745845'

n1 = re.findall('\d',data)
print(n1)
# ['7', '4', '3', '5', '8', '7', '9', '7', '5', '3', '8', '4', '6', '9', '7', '4', '5', '8', '4', '5']

# you want 2 digits

n2 = re.findall('\d{2}',data)
print(n2)
# ['74', '35', '87', '97', '53', '84', '69', '74', '58', '45']


n2 = re.findall('\d{2,4}',data)
print(n2)
# ['7435', '8797', '5384', '6974', '5845']
