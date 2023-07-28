
# single line suits

a = 10
if a>4:print(True)
else:print(False)
# True

# Chain multiple if statement in Python
# In Python, the if-elif-else condition statement has an elif blocks to chain multiple conditions one after another.
# This is useful when you need to check multiple conditions.

# With the help of if-elif-else we can make a tricky decision.
# The elif statement checks multiple conditions one by one and if the condition fulfills, then executes that code.

# Syntax of the if-elif-else statement:
#
# if condition-1:
#      statement 1
# elif condition-2:
#      stetement 2
# elif condition-3:
#      stetement 3
#      ...
# else:
#      statement


n = int(input('Enter on enumber:'))
if n==1:
    print(n,'is equal to 1')
elif n==2:
    print(n,'is equal to 2')
elif n==3:
    print(n,'is equal to 3')
elif n==4:
    print(n,'is equal to 4')
else:
    print(n,'is not equal to No one')


print('next line')

# Enter on enumber:4
# 4 is equal to 4
# next line


# Enter on enumber:6
# 6 is not equal to No one
# next line



# In the above example, the elif conditions are applied after the if condition.
# Python will evalute the if condition and if it evaluates to False then it will evalute
# the elif blocks and execute the elif block whose expression evaluates to True.
# If multiple elif conditions become True, then the first elif block will be executed.
