
num = int(input('Enter a number:'))
count = 0
while num > 0:
    digit = num % 10
    print('Now digit is:-->',digit)
    count = (count * 10) + digit
    print('Now count is:-->',count)
    num = num//10
    print('Now num is:-->',num)
print()
print(count)
# Enter a number:8686893988
# Now digit is:--> 8
# Now count is:--> 8
# Now num is:--> 868689398
# Now digit is:--> 8
# Now count is:--> 88
# Now num is:--> 86868939
# Now digit is:--> 9
# Now count is:--> 889
# Now num is:--> 8686893
# Now digit is:--> 3
# Now count is:--> 8893
# Now num is:--> 868689
# Now digit is:--> 9
# Now count is:--> 88939
# Now num is:--> 86868
# Now digit is:--> 8
# Now count is:--> 889398
# Now num is:--> 8686
# Now digit is:--> 6
# Now count is:--> 8893986
# Now num is:--> 868
# Now digit is:--> 8
# Now count is:--> 88939868
# Now num is:--> 86
# Now digit is:--> 6
# Now count is:--> 889398686
# Now num is:--> 8
# Now digit is:--> 8
# Now count is:--> 8893986868
# Now num is:--> 0
#
# 8893986868


# Enter a number:1234
# Now digit is:--> 4
# Now count is:--> 4
# Now num is:--> 123
# Now digit is:--> 3
# Now count is:--> 43
# Now num is:--> 12
# Now digit is:--> 2
# Now count is:--> 432
# Now num is:--> 1
# Now digit is:--> 1
# Now count is:--> 4321
# Now num is:--> 0
#
# 4321
