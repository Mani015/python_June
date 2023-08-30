
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-2) + fib(num-1)

num = int(input('Enter a fucntion:'))

for i in range(num):
    print(fib(i))

# Enter a fucntion:5
# 0
# 1
# 1
# 2
# 3
