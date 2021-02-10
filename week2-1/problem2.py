import argparse

parser = argparse.ArgumentParser(description = 'Congratulates your birthday')
parser.add_argument('--age', help = 'Enter your age', type = int)

args = parser.parse_args()

if args.age:
  print('Happy Birthday, you are already ​%d ​years old!' % args.age)
