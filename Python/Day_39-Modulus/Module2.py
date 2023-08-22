
# Approaching_2

from module1 import Addition,Subtraction

a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))

Operator = input('Enter + is addition: Enter - is subtraction:')

if Operator=='+':
    print('Addtiton of a,b:',Addition(a,b))
elif Operator=='-':
    print('subtraction of a,b is=',Subtraction(a,b))

else:
    print('You have given a invalid operator')
