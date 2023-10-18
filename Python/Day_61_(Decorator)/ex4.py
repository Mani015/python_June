
# 1).assigning function to a variable Name



def hello():
    print('hello Jhansi 😀')

Var = hello
print(Var)
# <function hello at 0x00000233D2F3EEE0>
print(Var())
# hello Jhansi 😀
#None


print()
def jhansi(x):
    return x

# 1st calling
var2 = jhansi(10)
print(var2)
# 10


# 2nd calling
print()
var3 = jhansi
print(var3)
# <function jhansi at 0x00000298616631F0>
print(var3(20))
# 20


