class A:
    def Method1(self):
        print('Mehtod1 of class A')
    def Method2(self):
        print("Method2 of class A")

class B(A):
    def Method1(self):
        print('Method1 of class B')
        super().Method1()


ob1 = B()
ob1.Method1()
ob1.Method2()

# Method1 of class B
# Mehtod1 of class A
# Method2 of class A