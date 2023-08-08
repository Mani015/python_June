def OutShell(num):
    if num==20:
        def Return_value():
            print(num, 'is equal to ',20)
    else:
        def Return_value():
            print(num,'is not equal to ',20)
    return Return_value()

OutShell(10)

# 10 is not equal to  20
