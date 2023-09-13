# TO get same method from the parent classes by using parent classname
class A:
    def method1(self):
        print('I am A class')
class B:
    def method1(self):
        print('I am B class')
class C(A,B):
    def method1(self):
        print('I am c class')
        #syn:classname.method(self)
        A.method1(self)
        B.method1(self)

ob1 = C()
ob1.method1()

# I am c class
# I am A class
# I am B class
