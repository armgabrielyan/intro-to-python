# 1)

a = [1, 4, 5, 7, 8, -2, 0, -1]

# 2)

print('At index 3:', a[3])
print('At index 5:', a[5])

# 3)

a_sorted = sorted(a, reverse = True)

print('Sorted a:', a_sorted)

# 4)

print('1...3:', a_sorted[1:4])
print('2...6:', a_sorted[2:7])

# 5)

del a_sorted[2:4]

# 6)

print('Sorted a:', a_sorted)

# 7)

b = ['grapes', 'Potatoes', 'tomatoes', 'Orange', 'Lemon', 'Broccoli', 'Carrot', 'Sausages']

# 8)

b_sorted = sorted(b)

print('Sorted b:', b_sorted)

# 9)

c = a[1:4] + b[4:7]

# 10

print('c:', c)
