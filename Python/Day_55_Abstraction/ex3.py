
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def Sleepin(self):
        pass
    @abstractmethod
    def Hunt(self):
        pass
    @abstractmethod
    def Sound(self):
        pass
    def Walk(self):
        print('Walk by using four legs')
class Lion(Animal):
    def Hunt(self):
        print('Hunting the other animals')

    def Sleepin(self):
        print('It is sleep 10hr for a day')

    def Sound(self):
        print('Sound like roar')

ob1 = Lion()
ob1.Hunt()
ob1.Sleepin()
# Hunting the other animals
