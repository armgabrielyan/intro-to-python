class Animal:
	def __init__(self, name, legs):
		self.name = name
		self.legs = legs


	def getName(self):
		print(f'My name is {self.name}')


	def getLegs(self):
		print(f'I have {self.legs} legs')


class Exnik(Animal):
	def __init__(self):
		super().__init__('Exnik', 4)


exnik = Exnik()
exnik.getName()
exnik.getLegs()
