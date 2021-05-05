class Car:
	def __init__(self, speed, color): # constructor
		self.speed = speed
		self.color = color


# create instances with attributes
ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

print(ford.speed, ford.color)
print(honda.speed, honda.color)
print(audi.speed, audi.color)