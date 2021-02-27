def before_after(func):
  def wrapper(*args, **kwargs):
    print('Before function call')
    res = func(*args, **kwargs)
    print(res)
    print('After function call')

    return res

  return wrapper

@before_after
def get_text():
  return 'Inside the function'

get_text()
