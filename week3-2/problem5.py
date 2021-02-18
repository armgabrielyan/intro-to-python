def avg_grade(name, *args):
  if args:
    avg = sum(args) / len(args)

    print(f'​{name}, your average grade is: {avg}​')
  else:
    print(f'No grades available for {name}')

avg_grade('Joe')
avg_grade('Doe', 90, 95, 100)
