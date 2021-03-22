correct_num = 5

for _ in range(10):
    guess = int(input('Enter guess: '))

    if correct_num == guess:
      print('That was a good guess!')
      break
