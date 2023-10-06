# finally
#Finally Keyword in Python
# Python provides a keyword finally, which is always executed after the try and except blocks.
# The final block always executes after the normal termination of the try block or after the try block terminates due to some exception.
try:
    with open('data.txt','r') as r1:
        print(r1.read())
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

# [Errno 2] No such file or directory: 'data.txt' Error occured
# I am always excute with/ without Error

