class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def anual_salary(self):
		return (self.pay*12)+self.bonus

class Employee: # no is_a() relationship in Salary and Employee
	def __init__(self, name, age, pay, bonus):
		self.name = name
		self.age = age
		self.obj_salary = Salary(pay, bonus) # composition
		'''salary class is contant and Employee class
		is container'''

	def total_salary(self):
		return self.obj_salary.anual_salary()

emp = Employee('Max', 25, 15000, 10000)
print(emp.total_salary())





