

price = 10000
print('Global variable:',price)

def Samsung():
    global price
    price = 12000
    print('local variable:',price)
Samsung()

if price==12000:
    print(price,'price has changed')
else:
    print(price,'price had no change')

# 12000 price has changed
