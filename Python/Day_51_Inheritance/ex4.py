# Method Resolution Order :
# Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.
#  Python supports classes inheriting from other classes. The class being inherited is called the Parent or Superclass,
# while the class that inherits is called the Child or Subclass.
#  In python, method resolution order defines the order in which the base classes are searched when executing a method.
# First, the method or attribute is searched within a class and then it follows the order we specified while inheriting.
# This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order).
#  While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an instance.
#  Thus we need the method resolution order.


# Same methods using insides of classes

class Parent1:
    def property1(self):
        print('This is super class1')
class Parent2:
    def property1(self):
        print('This is super class2')
class Child(Parent1,Parent2):
    def property1(self):
        print('This is is subclass')

ob1 = Child()
ob1.property1()
ob1.property1()
ob1.property1()
# This is is subclass
# This is is subclass
# This is is subclass