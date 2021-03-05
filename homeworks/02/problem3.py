def my_range(n):
    i = 0

    while i <= n:
        yield i
        i += 1

    yield 'there are no values left'


gen = my_range(4)

for i in range(7):
    print(next(gen))
