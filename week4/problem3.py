def list_func(list1):
  for value in list1:
    yield value

gen = list_func([16, 'Tom', False])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
