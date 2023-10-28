
import re
if re.search('you','if something is important enough, you do it even if the odds are not in your favour'):
    print('There is String')

# There is String

name = re.findall('you','if something is important enough, you do it even if the odds are not in your favour')

for i in name:
    print(i)
# you
# you
