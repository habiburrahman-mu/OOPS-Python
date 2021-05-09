'''

- Polygon is super class
- Rectangle and Triangle are sub-classes inherited from Polygon

'''

class Polygon:
	def set_value(self, __width = None, __height = None):
		self.__width = __width
		self.__height = __height

	'''
	As the __width and __height are private can not be accessed
	from sub-class. We need to get.
	'''

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height


class Rectangle(Polygon): # inheriting from polygon
	def area(self):
		return self.get_width() * self.get_height()

class Triangle(Polygon):  # inheriting from polygon
	def area(self):
		return self.get_width() * self.get_height() / 2

rect = Rectangle()
tri = Triangle()

rect.set_value(50, 40)  # all the methods and attributes are availble in sub-class
tri.set_value(50, 40)

print(rect.area())
print(tri.area())