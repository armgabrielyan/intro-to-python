d = { 'name': 'Armen', 'age': 15,'grades': [10, 8, 8, 4, 6, 7] }

weight_key = 'weight'

if weight_key in d.keys():
    print('Weight is:', d[weight_key])
else:
    n = int(input('Enter weight: '))
    d[weight_key] = n
