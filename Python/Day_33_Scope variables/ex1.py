
def Test1(x,y):
    print('x value is :',x)
    print('y values is :',y)
    def Test2(z):
        Sum = x + y + z
        print('Sum is:',Sum)
        for i in range(1,11):
            print(Sum,'X',i,'=',Sum*i)
    return Test2(2)
Test1(1,2)
# x value is : 1
# y values is : 2
# Sum is: 5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50

