def ArithGeoII(arr): 
    if len(arr) <= 2:
        return 'Arithmetic'
    i = 2
    gap = arr[1] - arr[0]
    multiplier = arr[1] / arr[0]
    isArithmetic = True
    isGeometric = True
    while i < len(arr):
        currGap = arr[i] - arr[i - 1]
        if gap == currGap:
            isArithmetic &= True
            isGeometric &= False
        elif arr[i - 1] * multiplier == arr[i]:
            isArithmetic &= False
            isGeometric &= True
        else:
            isArithmetic &= False
            isGeometric &= False
        i += 1
    if isArithmetic:
        return 'Arithmetic'
    elif isGeometric:
        return 'Geometric'
    else:
        return -1
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeoII([5, 10, 15])  
print ArithGeoII([2, 6, 18, 54])
print ArithGeoII([2, 6, 18, 36])
