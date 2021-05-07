class Rectangle:
	def __init__(self, height, width): # constructor
		self.__height = height
		self.__width = width

	def set_width(self, value):
		self.__width = value
	
	def get_width(self):
		return self.__width

	def set_height(self, value):
		self.__height = value

	def get_height(self):
		return self.__height

	def area(self):
		return self.__height*self.__width


# Create instances with attributes
rect1 = Rectangle(20, 40) 
rect2 = Rectangle(30, 10)

rect2.set_height(100)

print(rect1.area())
print(rect2.area())