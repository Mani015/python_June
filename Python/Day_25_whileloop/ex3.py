
num = 1
intial = 0

while intial<=10:
    if num%5==0 and num%9==0:
        print(num)
        intial+=1
    num+=1
print('loop complete')