import sys

print('Script name:', str(sys.argv[0]))
print('Number of arguments:', len(sys.argv) - 1)
print('Argument values:', ' '.join(sys.argv[1:]))
