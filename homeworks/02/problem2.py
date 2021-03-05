def add_its_me(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + ', it\'s me!'

    return wrapper

def add_u(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return '<u> ' + func(*args, **kwargs) + ' </u>'

    return wrapper


@add_u
@add_its_me
def hi():
    return 'Hi'


print(hi())
