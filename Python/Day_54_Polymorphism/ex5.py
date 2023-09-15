import multipledispatch as python
class Basic:
    @python.dispatch(int)
    def m1(self,x):
        self.x = x
        print(self.x + 10)

    @python.dispatch(int, int)
    def m1(self,x,y):
        self.x = x
        self.y = y

    @python.dispatch(int, int, int)
    def m1(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

# ob1 = Basic()
# ob1.m1(10,12)
# TypeError: m1() missing 1 required positional argument: 'z'

ob1 = Basic()
ob1.m1(12)
# 22
