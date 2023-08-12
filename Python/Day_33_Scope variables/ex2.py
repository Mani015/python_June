
# Built-in-scope:
# The Python interpreter has a number of functions and types built into it that are always available.


def Outer(x,y):
    z = x+y
    print('z  value is:',z)
    def Inner(a,b):
        c = a+b
        return 'c value is:',c
    New = Inner(2,3)
    list1 = list(New)
    print(list1)
    # print('Total sum of :',sum(list1))
Outer(1,2)

# z  value is: 3
# ['c value is:', 5]
