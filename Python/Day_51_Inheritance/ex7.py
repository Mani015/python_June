
# Multilevel inheritance
# In multilevel inheritance, a class inherits from a child class or derived class.
# Suppose three classes A, B, C. A is the superclass, B is the child class of A,
# C is the child class of B.
# In other words, we can say a chain of classes is called multilevel inheritance.

class Grand_Parent(object):
    def property1(self):
        print('This is grandfather class')
class Parent(Grand_Parent):
    def property2(self):
        print('This is parent class')
class Grnad_Child(Parent):
    def property3(self):
        print('This is child class')

ob1 = Grnad_Child()
ob1.property3()
ob1.property1()
ob1.property2()

# This is child class
# This is grandfather class
# This is parent class



# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, we can say one parent class and multiple child classes.
# -----------------------------------------------------------------------------------------------------------------------------
# Hybrid Inheritance
# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.