def power(max):
  for i in range(max + 1):
    yield 2 ** i

gen = power(3)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
