class Police_car:
    tax_value = 0.2


    def __init__(self, owner, price, pass_code):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code

        
    def tax(self):
        return self.price * self.tax_value


    def greeting(self):
        if self.__pass_code == 'admin':
            print(f'Welcome to your car, {self.owner}')


    def set_pass_code(self, pass_code):
        self.__pass_code = pass_code


    def get_pass_code(self):
        return self.__pass_code

    
p1 = Police_car('Policeman 1', 1400, 'not admin')
print(p1.tax())
print(p1.get_pass_code())
p1.greeting()

p2 = Police_car('Policeman 2', 2600, 'admin')
print(p2.tax())
print(p2.get_pass_code())
p2.greeting()
