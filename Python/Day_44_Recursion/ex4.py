import sys

# TO control recursion limit
sys.setrecursionlimit(100)

i = 0
def New():
    global i
    i+=1
    print('Hello New',i)
    New()
New()


