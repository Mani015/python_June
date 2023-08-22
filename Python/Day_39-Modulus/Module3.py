
# Approaching_3
from module1 import *

# from module1 import Addition,Subtraction,multiplication,division,floordivision,modulus

a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))

Operator = input('Enter + is addition: Enter - is subtraction: enter * multi,enter / divi'
                 ',enter // floor,enter modulus')

if Operator=='+':
    print('Addtiton of a,b:',Addition(a,b))
elif Operator=='-':
    print('subtraction of a,b is=',Subtraction(a,b))
elif Operator=='*':
    print('multi of a,b is=',multiplication(a,b))
elif Operator=='/':
    print('division of a,b is=',division(a,b))
elif Operator=='//':
    print('floor of a,b is=',floordivision(a,b))
elif Operator=='%':
    print('modulus of a,b is=',modulus(a,b))
else:
    print('You have given a invalid operator')
