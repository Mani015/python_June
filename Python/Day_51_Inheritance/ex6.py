
# class Parent1:
#     def property2(self):
#         print('This is super class1')
# class Parent2:
#     def property2(self):
#         print('This is super class2')
# class Child(Parent2,Parent1):
#     pass
# ob1 = Child()
# ob1.property2()
# ob1.property2()
# ob1.property2()

# This is super class2
# This is super class2
# This is super class2


# -------------------------------------------

class Parent1:
    def property2(self):
        print('This is super class1')
class Parent2:
    pass
class Child(Parent2,Parent1):
    pass
ob1 = Child()
ob1.property2()
ob1.property2()
ob1.property2()

# This is super class1
# This is super class1
# This is super class1