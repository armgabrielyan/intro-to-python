def max(*args):
    if len(args) == 0:
        return 'no numbers given'
    
    m = args[0]

    for arg in args:
        if arg > m:
            m = arg

    return m


print(max())
print(max(5, 12, 3, 6, 7, 10, 9))
