import argparse

parser = argparse.ArgumentParser(description = 'Simple text printing')
parser.add_argument('text', help = 'some random text', type = str)

args = parser.parse_args()

print('The given string:', args.text)
print('All lowercase:', args.text.lower())
print('All uppercase:', args.text.upper())
