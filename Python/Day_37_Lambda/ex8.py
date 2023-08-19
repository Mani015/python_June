
x = 'i am a python developer'
# for i in x:
#     if i in 'aeiou':
#         print(i)



def Vowels(name):
    if name in 'aeiou':
        return name

f1 = list(filter(Vowels,x))
print(f1)

# ['i', 'a', 'a', 'o', 'e', 'e', 'o', 'e']
