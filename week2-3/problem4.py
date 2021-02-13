name = 'Batman'
age = 15
password = 'qwerty&123'

if name == 'Batman':
    print('Welcome Mr. Batman!')

if age < 16:
    print(f'Dear {name}, you are too young to register')

if password.find('*') == -1 or password.find('&') == -1:
    print('Please enter a different password')
