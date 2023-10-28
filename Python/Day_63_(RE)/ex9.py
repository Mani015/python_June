
stu_info = 'Jhansi age is 24 Anusha age is 22' \
           'Laxmi age is 28 Priya age is 20 Prasad age is 19 Girish age is 20'

import re
age = re.findall('\d{2}',stu_info)
# print(age)
# ['24', '22', '28', '20', '19', '20']


names = re.findall('[A-Z][a-z]*',stu_info)
print(names)

#['Jhansi', 'Anusha', 'Laxmi', 'Priya', 'Prasad', 'Girish']


dict = {}

var = 0
for i in names:
    dict[i] = age[var]
    var+=1

print(dict)

# {'Jhansi': '24', 'Anusha': '22', 'Laxmi': '28', 'Priya': '20', 'Prasad': '19', 'Girish': '20'}
