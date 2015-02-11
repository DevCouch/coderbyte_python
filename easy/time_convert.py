def test(arg):
  hour = arg // 60
  minute = arg % 60
  return str(hour) + ':' + str(minute)

print test(180)
