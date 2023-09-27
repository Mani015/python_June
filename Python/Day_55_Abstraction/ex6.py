

# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class Phone(ABC):
    def Caution(self):
        print('Please charge only 2hr')

class Realme(Phone):
    def Caution(self):
        print('Follow the parent method')
        Phone.Caution(self)



ob1 = Realme()
ob1.Caution()
# Follow the parent method
# Please charge only 2hr


# 12345
# 54321
