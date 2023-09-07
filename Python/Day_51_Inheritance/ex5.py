# same methods derived parent1,parent2 classes
# class Parent1:
#     def property1(self):
#         print('This is super class1')
# class Parent2:
#     def property1(self):
#         print('This is super class2')
# class Child(Parent1,Parent2):
#     def property2(self):
#         print('This is is subclass')
# ob1 = Child()
# ob1.property1()
# ob1.property1()
# ob1.property1()

# This is super class1
# This is super class1
# This is super class1





class Parent1:
    def property1(self):
        print('This is super class1')
class Parent2:
    def property1(self):
        print('This is super class2')
class Child(Parent2,Parent1):
    def property2(self):
        print('This is is subclass')
ob1 = Child()
ob1.property1()
ob1.property1()
ob1.property1()
# This is super class2
# This is super class2
# This is super class2
