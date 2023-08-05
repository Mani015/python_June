

Intial = 0
Attempts = 4

while Attempts>Intial:
    password = int(input('Enter your password:'))
    if password==1234:
        print('Screen is open')
        break
    Intial+=1
else:
    print('Your limits complete')

