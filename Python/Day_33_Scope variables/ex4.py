g1 = 12
print('global variable:',g1)
def Outer(x,y):
    z = x+y # 3
    print('z  value is:',z)
    print('global variable:', g1)
    def Inner(a,b):
        c = a+b
        print('global variable:', g1)
        return c  # 5
    New = Inner(2,3)
    print('global variable:', g1)
    list1 = [New,z,x,y,g1]
    print(list1)
    print('Total sum of :',sum(list1))
Outer(1,2)
print('global variable:',g1)

# global variable: 12
# z  value is: 3
# global variable: 12
# global variable: 12
# global variable: 12
# [5, 3, 1, 2, 12]
# Total sum of : 23
# global variable: 12