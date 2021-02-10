str1 = 'How are you John?'
name = 'Armen'

str2 = str1[:12] + name + str1[-1]

print('The first way:', str2)

str2 = str1.replace('John', name)

print('The second way:', str2)
