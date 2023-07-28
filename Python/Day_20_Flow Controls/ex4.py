
# Nested if-else statement
# In Python, the nested if-else statement is an if statement inside another if-else statement.
# It is allowed in Python to put any number of if statements in another if statement.
#
# Indentation is the only way to differentiate the level of nesting.
# The nested if-else is useful when we want to make a series of decisions.
#
# Syntax of the nested-if-else:
#
# if conditon_outer:
#     if condition_inner:
#         statement of inner if
#     else:
#         statement of inner else:
#     statement ot outer if
# else:
#     Outer else
# statement outside if block



x1 = 12
if x1<10:
    print(x1 ,' is not equal to 10')
    if x1<-12:
        print(False)
    elif x1==12:
        print(x1,'is equal to ',x1)
    else:
        print('You are wrong')
else:
    print(False)

# 12  is not equal to 10
# 12 is equal to  12










