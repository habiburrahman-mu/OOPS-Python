class Person:
	def __init__(self, person_name: str, year_of_birth: int, ht_inches = None):
		self.__name = person_name
		self.__date_of_birth = year_of_birth
		self.__height = ht_inches
		self.abc = None
		
	def get_name(self):
		return self.__name
		
	def get_summary(self):
	    return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height if self.__height is not None else 'Invalid'}"

	def set_name(self, new_name):
		if(self.__has_any_number(new_name)) :
			print("Sorry Person name cannot have numbers")
			return
		self.__name = new_name

	def get_year_of_birth(self):
		return self.__date_of_birth

	def __has_any_number(self, string):
		return "0" in string

person_list = []
person_list.append(Person('Habib', 1997, 67))
person_list.append(Person('Bar1', 1971))
person_list.append(Person('Foo', 1960, 72))
person_list.append(Person('Habib5', 1991))

for person in person_list:
	if person.get_year_of_birth() >= 1990:
		print(person.get_summary())

# class Student(Person):
# 	def __init__(self):
		
# this is new comment