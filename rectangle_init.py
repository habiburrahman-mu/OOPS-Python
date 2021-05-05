class Rectangle:
	def __init__(self, height, width): # constructor
		self.height = height
		self.width = width


# Create instances with attributes
rect1 = Rectangle(20, 40) 
rect2 = Rectangle(30, 10)

print(rect1.height*rect1.width)
print(rect2.height*rect2.width)