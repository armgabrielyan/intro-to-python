import argparse

parser = argparse.ArgumentParser(description = 'Replace given word in the text')
parser.add_argument('text', help = 'some random text', type = str)
parser.add_argument('first_word', help = 'first word', type = str)
parser.add_argument('second_word', help = 'second', type = str)

args = parser.parse_args()

output = args.text.replace(args.first_word, args.second_word)

print('The given text:', args.text)
print('First word:', args.first_word)
print('Second word:', args.second_word)
print('Output string:', output)
