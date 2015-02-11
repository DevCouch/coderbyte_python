def test(arg):
    chars = list(arg)
    chars.sort()
    print chars
    return ''.join(chars)

print test("hello")
