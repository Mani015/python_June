
# Concrete Methods in Abstract Base Classes
# Concrete classes contain only concrete (normal)methods whereas abstract classes
# may contain both concrete methods and abstract methods.
# The concrete class provides an implementation of abstract methods,
# the abstract base class can also provide an implementation by invoking the methods via super().
# Let look over the example to invoke the method using super():

# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class R(ABC):
	def rk(self):
		print("Abstract Base Class")

class K(R):
	def rk(self):
		super().rk()
		print("subclass ")

# Driver code
r = K()
r.rk()
