
# Iterate using while loop
l1 = map(lambda x: x**2,range(1,11))


# while True:
#     var = next(l1)
#     print(var)

# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# Traceback (most recent call last):
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_62_Generator\ex9.py", line 7, in <module>
#     var = next(l1)
# StopIteration



# using Try and excpet block

while True:
    try:
        var = next(l1)
        print(var)
    except StopIteration as stop:
        print(stop,'Error Occured')
        break

print('Loop Completed')

