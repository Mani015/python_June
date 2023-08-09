
# Default Arguments in Python
# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# Default arguments become optional during the function calls.
# If we provide a value to the default arguments during function calls, it overrides the default value.
# The function can have any number of default arguments.
# Default arguments should follow non-default arguments.


def Padma(house='Kadapa',phone=1234567890,adhar=98765432112,pan='PPx01234x'):
    print('House name:',house)
    print('phone no:',phone)
    print('adhar no:',adhar)
    print('pan number:',pan)
# Default arguments become optional during the function calls.
Padma()
# House name: Kadapa
# phone no: 1234567890
# adhar no: 98765432112
# pan number: PPx01234x
