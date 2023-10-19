# using yield keyword
def Table(num):
    for i in range(1,11):
        yield f'{num} X {i} = {num * i}'
# num = int(input('Enter a number'))

# new = Table(num)
# print(new)
# Enter a number7
# <generator object Table at 0x0000017399A077B0>
# for i in new:
#     print(i)
# Enter a number7
# 7 X 1 = 7
# 7 X 2 = 14
# 7 X 3 = 21
# 7 X 4 = 28
# 7 X 5 = 35
# 7 X 6 = 42
# 7 X 7 = 49
# 7 X 8 = 56
# 7 X 9 = 63
# 7 X 10 = 70




# USING RETURN

def new_table(num):
    for i in range(1,11):
        return f'{num} x {i} = {num*i}'

print(new_table(6))
# 6 x 1 = 6
