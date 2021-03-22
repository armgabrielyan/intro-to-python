class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    
    def getDesc(self):
        print(f'A {self.color} circle with radius​ {self.radius}')


circle1 = Circle(5, 'red')
circle2 = Circle(12, 'yellow')

circle1.getDesc()
circle2.getDesc()
