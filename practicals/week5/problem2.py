class Employee:
    def __init__(self, name, last_name, monthly_salary):
        self.name = name
        self.last_name = last_name
        self.__monthly_salary = monthly_salary


    def getFullName(self):
        return f'{self.name} {self.last_name}'


    def annual_salary(self):
        salary = 12 * self.__monthly_salary

        return 'High' if salary > 100 else 'Low'


employee1 = Employee('John', 'Doe', 8)
print(employee1.getFullName())
print(employee1.annual_salary())

employee2 = Employee('Jane', 'Dane', 12)
print(employee2.getFullName())
print(employee2.annual_salary())
