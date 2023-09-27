
# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass
	def Type(self):
		print('These all are ploygons')


class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")


class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")


class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")


class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()
R.Type()

K = Quadrilateral()
K.noofsides()
K.Type()

R = Pentagon()
R.noofsides()
R.Type()
K = Hexagon()
K.noofsides()
K.Type()
