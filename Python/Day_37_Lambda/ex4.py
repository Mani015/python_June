

names = ['jhansi','sravani','anusha','girish']
# for i in names:
#     print(i.upper())

def Upper(name):
    return name.upper()

N1 = map(Upper,names)
# print(N1)
# <map object at 0x000001E13E00B160>

print(set(N1))
# {'GIRISH', 'ANUSHA', 'JHANSI', 'SRAVANI'}
