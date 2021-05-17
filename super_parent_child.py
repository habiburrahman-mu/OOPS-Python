class Parent:
	def __init__(self, name):
		print("Parent __init__", name)

class Parent2:
	def __init__(self, name):
		print("Parent2 __init__", name)

class Child(Parent, Parent2):
	def __init__(self):
		print("Child __init__")
		super().__init__('Habib')
		Parent2.__init__(self, 'Habib')
		Parent.__init__(self, 'Tom')

child = Child()
# method resolution order
print(Child.__mro__) # returns -> 
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Parent2'>, <class 'object'>)

