def test(arg):
    lastA = 0
    index = 0
    isvalid = 0
    for ch in arg:
        if ch == 'a':
            lastA = index
        elif ch == 'b':
            if index - 4 == lastA:
                isvalid |= 1
            else:
                isvalid |= 0
        index += 1
    return 'true' if isvalid else 'false'
            

print test("Laura sobs")
print test("after badly")
print test("123advb")
print test("123adzvb")
print test("abccccazzzb")
