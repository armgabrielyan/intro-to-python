values = ['a', 0, 2]

for value in values:
    try:
        reciprocal = 1 / value

        print(f'The entry is {value}')
        print(f'The reciprocal of ​{value} ​is ​{reciprocal}')
    except Exception as e:
        print(f'The entry is {value}')
        print(f'Oops! {type(e).__name__}: {e}')
