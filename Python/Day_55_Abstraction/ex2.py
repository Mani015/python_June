# How Abstract Base classes work :
# By default, Python does not provide abstract classes.
# Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
# ABC works by decorating methods of the base class as abstract and then registering concrete classes as
# implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.


from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def Sleepin(self):
        print('sleep')

    @abstractmethod
    def Hunt(self):
        print('Brutal ')

    @abstractmethod
    def Sound(self):
        print('Sound')

# class Lion(Animal):
#     pass
# ob1 = Lion()

# TypeError: Can't instantiate abstract class Lion with abstract methods Hunt, Sleepin, Sound

class Lion(Animal):
    def Hunt(self):
        print('Hunting the other animals')

ob1 = Lion()
ob1.Hunt()
# TypeError: Can't instantiate abstract class Lion with abstract methods Sleepin, Sound
