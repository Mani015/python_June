
# An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation.
# While we are designing large functional units we use an abstract class.
# When we want to provide a common interface for different implementations of a component, we use an abstract class.


# Why use Abstract Base Classes :
# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.
# This capability is especially useful in situations where a third-party is going to provide implementations,
# such as with plugins, but can also help you when working in a large team or with a large code-base
# where keeping all classes in your mind is difficult or not possible.







class Animal:
    def Eating(self):
        print('For day eating 3 4 times')
    def Sleepin(self):
        print('10hr per a day')
    def Hunting(self):
        print('Hunting the another creeps')
    def Sound(self):
        print('20db')

class Tiger(Animal):
    def Eating(self):
        print('Chicken pakoda')
    def Sound(self):
        print('Sound like a Roar')
        super().Sound()
    def Hunting(self):
        print('Hunting the another animals')

ob1 = Tiger()
ob1.Sound()
# Sound like a Roar
# 20db