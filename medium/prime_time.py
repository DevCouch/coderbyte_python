def test(arg):
    if arg == 1 or arg == 2:
        return 'true'
    if (arg - 1) % 4 == 0 or (arg - 3) % 4 == 0:
        return 'true'
    else:
        return 'false'
    
print test(1)
print test(2)
print test(5)
print test(6)
print test(27)
