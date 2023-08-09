
def Padma(house='Kadapa',phone=1234567890,adhar=98765432112,pan='PPx01234x'):
    print('House name:',house)
    print('phone no:',phone)
    print('adhar no:',adhar)
    print('pan number:',pan)
# Default arguments become optional during the function calls.
# Padma('Rayalaseema')
# If we provide a value to the default arguments during function calls, it overrides the default value.
# House name: Rayalaseema
# phone no: 1234567890
# adhar no: 98765432112
# pan number: PPx01234x


Padma('Rayalaseema',1122334455)
# House name: Rayalaseema
# phone no: 1122334455
# adhar no: 98765432112
# pan number: PPx01234x

