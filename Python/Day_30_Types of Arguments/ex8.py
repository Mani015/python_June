
# If you are updating the  particular default arguments using the keyword arguments:

def Phone(price=10000,ram=6,rom=128,battery=5000):
    print('price is :',price)
    print('Random Access Memory is :',ram)
    print('Read only memory is :',rom)
    print('battery is : ',battery)
# Phone()
# price is : 10000
# Random Access Memory is : 6
# Read only memory is : 128
# battery is :  5000

# If you are Updating the phone price:
Phone(price=30000)
# price is : 30000
# Random Access Memory is : 6
# Read only memory is : 128
# battery is :  5000

Phone(price=40000,battery=6000)
# price is : 10000
# Random Access Memory is : 6
# Read only memory is : 128
# battery is :  6000

# price is : 40000
# Random Access Memory is : 6
# Read only memory is : 128
# battery is :  6000