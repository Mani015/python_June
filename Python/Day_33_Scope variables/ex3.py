def Outer(x,y):
    z = x+y # 3
    print('z  value is:',z)
    def Inner(a,b):
        c = a+b
        return c  # 5
    New = Inner(2,3)
    list1 = [New,z,x,y]
    print(list1)
    print('Total sum of :',sum(list1))
Outer(1,2)

# z  value is: 3
# [5, 3, 1, 2]
# Total sum of : 11
