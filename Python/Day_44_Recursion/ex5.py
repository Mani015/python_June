

# Factorial


def Fact(num):
    if num==0:
        return 1
    else:
        return num * Fact(num-1)

print(Fact(5))

# 120

