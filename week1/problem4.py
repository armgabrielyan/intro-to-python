text = input('Enter text whose length is odd and greater than or equal to 7: ')

length = len(text)
middle = text[length // 2 - 1:length // 2 + 2]

print('The old string', text)
print('Middle 3 characters', middle)
print('The old string', text[:length // 2 - 1] + middle.upper() + text[length // 2 + 2:]) 
