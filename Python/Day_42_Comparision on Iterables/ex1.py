
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Here, ord() and chr() are built-in functions.
# Visit here to know more about built-in functions in Python.
# print('a'>'A')
# True
# print('A'>='a')
# False

# What is the ASCII value?
# ASCII stands for “American Standard Code For Information Interchange”.
# It contains only 128 characters that are used to represent different symbols,
# decimal digits and English alphabets in a computer.
# print(ord('a')) # 97
# print(ord('A'))
# 65
# print(ord('!'))# 33

# print(ord('1'))
# 49
# print('1'>1)
# TypeError: '>' not supported between instances of 'str' and 'int'
# print('1'>'2')
# False

# print(chr(65))
#A



# programm for calculating electrcity bill in python
unit = int(input('please enter  the number of units you consumed ina month:'))
if unit<=100:
    payamount = unit*1.5
    fixedcharge = 25.00
elif unit<=200:
    payamount = (100*1.5) + (unit-100)*2.5
    fixedcharge = 50.00
elif unit<=300:
    payamount =(100*1.5) + (unit-100)*2.5 + (unit-200)*4
    fixedcharge = 75.00
elif unit<=350:
    payamount = (100 * 1.5) + (unit - 100) * 2.5 + (unit - 200) * 4 + (unit-300)*5
    fixedcharge = 100.00
else:
    payamount = 0
    fixedcharge = 1500.00
Total  = payamount + fixedcharge
print('electricty bill=',Total)

