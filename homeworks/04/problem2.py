class My_Time:
	def __init__(self, t):
		self.t = t


	def printTime(self):
		print(f'The current time is {self.t}')


class My_Date:
	def __init__(self, d):
		self.d = d


	def printDate(self):
		print(f'The current date is {self.d}')


class Date_Time(My_Date, My_Time):
	def __init__(self, d, t):
		My_Date.__init__(self, d)
		My_Time.__init__(self, t)


date_time = Date_Time('13.03.2013', '12 PM')
date_time.printTime()
date_time.printDate()
