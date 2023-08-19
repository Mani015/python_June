
# using range

def Work(S):
    if S%2==0:
        if S==None:
            pass
        return S*S

x = range(1,11)

# Even_Square = map(Work,x)

# print(list(Even_Square))
# [None, 4, None, 16, None, 36, None, 64, None, 100]

x1 = map(Work,range(1,11))
print(list(x1))

