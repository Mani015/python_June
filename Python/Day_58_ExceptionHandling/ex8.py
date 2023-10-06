
try:
    x1 = int(input('Enter a number:'))

except ValueError as value:
    print(value,'Error occured')
except ZeroDivisionError as zero:
    print(zero,'Error occured')
except NameError as name:
    print(name,'Error occured')
except:
    print('Error will be occured')
except FileNotFoundError as File:
    print(File,'Error occured')
except TypeError as Type:
    print(Type,'Error occured')

else:
    print('There is no error, it ll excute')
finally:
    print('I am always excute with/ without Error')
# SyntaxError: default 'except:' must be last