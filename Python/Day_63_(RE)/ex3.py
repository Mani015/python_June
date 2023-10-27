# The findall() Function
# The findall() function returns a list containing all matches.

s1 = "The PAST can't be changed but you can change your FUTURE."
import re
f1 = re.findall('FUTURE',s1)
print(f1)
# ['FUTURE']

f2 = re.findall('can',s1)
print(f2)
# ['can', 'can']

