st1 = input('Enter one quotation:')
vowels = 0
consonants = 0
spaces = 0

for i in st1:
    if i in 'aeiou' or i in 'AEIOU':
        vowels+=1
    elif i==' ':
        spaces+=1
    else:
        consonants+=1

print('voewls:',vowels)
print()
print('spaces',spaces)
print()
print('consonants:',consonants)

# Enter one quotation:If You wish to be good You will be Good
# voewls: 14
# spaces 9
# consonants: 16



# Enter one quotation:If you Do good It will come back to you in Unexpected Ways
# voewls: 20
#
# spaces 12
#
# consonants: 26