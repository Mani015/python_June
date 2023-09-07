# WITH  INHERITANCE:

class Parent:
    def Property1(self):
        print('I am Parent class')
class Child(Parent):  # parent class is using insdie of child class , child class is a inherit
    def Property2(self):
        print('I am a Derived class')


ob1 = Child()   # who is inherit to make object
ob1.Property2() #I am a Derived class
ob1.Property1()
# I am Parent class
