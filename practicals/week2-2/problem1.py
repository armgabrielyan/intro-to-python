list1 = ['hello', 1, True]

value1 = input('Enter the first value: ')
value2 = input('Enter the second value: ')

list1_after = list1.copy()
list1_after.extend([value1, value2])

print('Before', list1)
print('After', list1_after)
