
# raw string

print('\tTab')
print()
print(r'\tTab')
# 	Tab
# \tTab

# raw string
# In programming, a raw string is a string literal that treats backslashes ()
# as literal characters instead of escape characters.
# This means that any backslashes in a raw string are interpreted as part of the string itself,
# rather than having special meaning.


name = 'python developer \\\\\jhansi'
print('Without raw string:  ','python developer \\\\\jhansi')
# python developer \\jhansi

print('With raw string:  ',r'python developer \\\\\jhansi')

# Without raw string:   python developer \\\jhansi
# With raw string:   python developer \\\\\jhansi
