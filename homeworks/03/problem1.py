class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    
    def compareCar(self, car2):
        if self.max_speed > car2.max_speed:
          return f'car1({self.model}) is better than car2({car2.model})'

        return f'car2({car2.model}) is better than car1({self.model})'


car1 = Car('Dodge Challenger', 'red', 250)
car2 = Car('Dodge Charger', 'black', 300)

print(car1.compareCar(car2))
print(car2.compareCar(car1))
