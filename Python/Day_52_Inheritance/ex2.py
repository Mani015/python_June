# TO get same method from the parent classes by using super() function


class Grand_Parent:
    def M1(self):
        print('I am Grand_Parent class')
class Parent(Grand_Parent):
    def M1(self):
        print('I am Parent class')
        super().M1()
        
class Child(Parent):
    def M1(self):
        print('I am Child class')
        super().M1()
ob1 = Child()
ob1.M1()
# I am Child class
# I am Parent class
# I am Grand_Parent class

