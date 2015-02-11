def test(arg):
    if len(arg) <= 2:
        return 'Arithmetic'
    i = 2
    gap = arg[1] - arg[0]
    multiplier = arg[1] / arg[0]
    isArithmetic = 1
    isGeometric = 1
    while i < len(arg):
        currGap = arg[i] - arg[i - 1]
        if gap == currGap:
            isArithmetic &= 1
            isGeometric &= 0
        elif arg[i - 1] * multiplier == arg[i]:
            isArithmetic &= 0
            isGeometric &= 1
        else:
            isArithmetic &= 0
            isGeometric &= 0
        i += 1
    if isArithmetic == 1:
        return 'Arithmetic'
    elif isGeometric == 1:
        return 'Geometric'
    else:
        return -1

print test([5, 10, 15])
print test([2, 6, 18, 54])
print test([2, 6, 18, 36])
