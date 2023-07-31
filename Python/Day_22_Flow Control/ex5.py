
# Find out vowels and consonants

s1 = input('Enter string:')

vowels = 0
consonants = 0

for i in s1:
    if i in 'aeiou':
        vowels+=1
    else:
        consonants+=1

print('TOtal vowels:',vowels)
print()
print('Total consonants:',consonants)

# TOtal vowels: 7
#
# Total consonants: 20
