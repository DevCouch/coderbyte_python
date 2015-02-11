def test(arg):
    vowels = 'aeiou'
    return sum(arg.count(c) for c in vowels)

print test("abc")
print test("here")
