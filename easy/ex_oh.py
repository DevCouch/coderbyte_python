def test(arg):
    arg = arg.lower()
    xcount = arg.count('x')
    ocount = arg.count('o')
    return 'true' if xcount == ocount else 'false'
    
print test("o")
print test("x")
print test("ox")
print test("oxxo")
print test("oxox")
print test("oxxxoo")
