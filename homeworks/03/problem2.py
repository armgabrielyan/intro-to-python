import time


def timing(func):
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        res = func(*arg, **kwargs)
        t2 = time.time()

        print(f'Elapsed time: {t2 - t1} seconds')

        return res
        
    return wrapper


class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password


    def Greeting(self, second_person):
      print(f'Welcome dear {second_person.name}.')


    @timing
    def Goodbye(self):
      print(f'Bye everyone!')


    def Favourite_num(self, num1):
      return f'My favourite number is {num1}'


    def Read_file(self, filename):
      f = open(f'{filename}.txt', 'r')

      return f.read()


    def set_password(self, password):
        self.__password = password


    def get_password(self):
        return self.__password


person = Person('John', 'Doe', 18, 'Male', True, '123456')
person.Greeting(person)
person.Goodbye()
print(person.Favourite_num(10))
print(person.get_password())
person.set_password('qwerty')
print(person.get_password())

print(person.Read_file('test'))
