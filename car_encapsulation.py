class Car:
	def __init__(self, speed, color): # constructor
		self.__speed = speed
		self.__color = color

	def set_speed(self, value):
		self.__speed = value

	def get_speed(self):
		return self.__speed

	def set_color(self, value):
		self.__color = value

	def get_color(self):
		return self.__color


# create instances with attributes
ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

ford.set_speed(300)

print(ford.get_speed(), ford.get_color())
print(honda.get_speed(), honda.get_color())
print(audi.get_speed(), audi.get_color())