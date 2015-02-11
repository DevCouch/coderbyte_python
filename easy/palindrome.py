def test(str):
    str = str.replace(' ', '')
    rev = str[::-1]
    return 'true' if str == rev else 'false'
    

print test("never odd or even")
