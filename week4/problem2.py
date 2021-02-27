def convert_to_lowercase(func):
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs).lower()

    return result

  return wrapper

def add_additional_info(func):
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs) + '!!! Welcome to the party.'

    return result

  return wrapper

@add_additional_info
@convert_to_lowercase
def hi_everyone():
  return 'HI EVERYONE'

print(hi_everyone())
