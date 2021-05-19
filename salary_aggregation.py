class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def anual_salary(self):
		return (self.pay*12)+self.bonus

class Employee: # no is_a() relationship in Salary and Employee
	def __init__(self, name, age,salary):
		self.name = name
		self.age = age
		self.obj_salary = salary # aggregation

	def total_salary(self):
		return self.obj_salary.anual_salary()

salary = Salary(15000, 10000)
emp = Employee('Max', 25, salary) # aggregation
print(emp.total_salary())





