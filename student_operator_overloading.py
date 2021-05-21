class Student:

	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self, other): # operator overloading
		m1 = self.m1+other.m1
		m2 = self.m2+other.m2
		s3 = Student(m1, m2)
		return s3

	def __gt__(self, other): # operator overloading
		r1 = self.m1+self.m2
		r2 = other.m1+other.m2
		if r1>r2:
			return True
		else:
			return False

	def __str__(self): # operator overloading
		return '{} {} '.format(self.m1, self.m2)

s1 = Student(58,69)
s2 = Student(60, 65)

s3 = s1 + s2 # calling Student.__add__() method
print(s3) # # calling Student.__str__() method

if s1>s2: # calling Student.__gt__() method
	print("s1 wins")
else:
	print("s2  wins")
