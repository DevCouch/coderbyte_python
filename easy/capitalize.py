def test(arg):
  strings = arg.split(' ')
  return ' '.join(string.capitalize() for string in strings)


print test('hello world')
