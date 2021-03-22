from abc import abstractmethod

class Bird:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	@abstractmethod
	def fly(self):
		pass


class Hav(Bird):
	def __init__(self, name, weight):
		super().__init__(name, weight)


	def fly(self):
		print('I believe I can fly')


hav = Hav('H', 2)
hav.fly()
