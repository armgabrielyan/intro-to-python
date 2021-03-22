class Animal:
	def __init__(self, name):
		self.name = name


	def move(self):
		print('I can move')


class Dog(Animal):
	def __init__(self):
		super().__init__('Dog')


dog = Dog()
dog.move()


class Dog(Animal):
	def __init__(self):
		super().__init__('Dog')


	def move(self):
		print('I can run really fast')


dog = Dog()
dog.move()
