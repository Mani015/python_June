
# Multiple Inheritance
#
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.



class Parent1:
    def property1(self):
        print('This is super class1')
class Parent2:
    def property2(self):
        print('This is super class2')
class Child(Parent1,Parent2):
    def property3(self):
        print('This is is subclass')

ob1 = Child()
ob1.property1()
ob1.property2()
ob1.property3()
# This is super class1
# This is super class2
# This is is subclass
