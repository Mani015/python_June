
import string

# Only digits:
print(string.digits)
# 0123456789

# Only Hexadecimal
print(string.hexdigits)
# 0123456789abcdefABCDEF
print(string.octdigits)
# 01234567

print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print(string.whitespace)
# 
#
# 

print(string.__all__)
# ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace', 'Formatter', 'Template']
x = 'python developer'
print(string.capwords(x,sep=','))
# Python Developer

a = 'mango,apple,pineapple,graphes,sapota'
print(string.capwords(a,sep=','))
# Mango,Apple,Pineapple,Graphes,Sapota
print(string.capwords(a,sep='a'))
# MaNgo,aPple,pineaPple,graPhes,saPota

x = [[1,2,3,4,5],[11,22,33,44,55]]
print(x)
for i in x:
    print(i)