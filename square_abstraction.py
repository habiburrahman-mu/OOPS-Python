# for abstraction we need to import ABC method
from abc import ABC, abstractmethod

class Shape(ABC): # inherit from ABC method
	
	@abstractmethod
	def area(self): pass

	@abstractmethod
	def perimeter(self): pass

class  Square(Shape):
	def __init__(self, side):
		self.__side = side

	def area(self):
		return self.__side * self.__side

	def perimeter(self):
		return  4 * self.__side

square = Square(5)
print(square.area())
print(square.perimeter())