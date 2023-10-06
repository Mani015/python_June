# else:
# Try with Else Clause
# In Python, you can also use the else clause on the try-except block which must be present after all the except clauses.
# The code enters the else block only if the try clause does not raise an exception.

try:
    x1 = int(input('Enter a number:'))

except ValueError as value:
    print(value,'Error occured')
except ZeroDivisionError as zero:
    print(zero,'Error occured')
except NameError as name:
    print(name,'Error occured')
except FileNotFoundError as File:
    print(File,'Error occured')
except TypeError as Type:
    print(Type,'Error occured')

else:
    print('There is no error, it ll excute')
finally:
    print('I am always excute with/ without Error')

# Enter a number:1
# There is no error, it ll excute
# I am always excute with/ without Error