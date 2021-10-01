class Hello:
	def __init__(self, name):
		self.a = 10
		self.__b = 20
		self.__c = 30

	def __private_method(self): # private method
		print('private')

	def public_method(self):
		print(self.__c)
		print('public')
		self.__private_method()

hello = Hello('name')
hello.public_method()
