
# range of matching
import re
s4 = "Running, cooking, eating, dancing,singing,amazing"

x1 = re.findall('[a-z]ing',s4)
for i in x1:
    print(i)
# ning
# king
# cing
# sing
