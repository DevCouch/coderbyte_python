def test(arg):
    val = ''
    currCh = ''
    currIndex = 0
    for ch in arg:
        if currCh == '':
            currCh = ch
            currIndex += 1
        elif currCh == ch:
            currIndex += 1
        else:
            val += str(currIndex) + currCh
            currIndex = 1
            currCh = ch
    val += str(currIndex) + currCh
    return val
    

print test("aabbcde")
print test("wwwbbbw")
