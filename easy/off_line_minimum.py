def OffLineMinimum(strArr): 
    digitArr = []
    result = []
    for ch in strArr:
        if ch.isdigit():
            digitArr.append(ch)
        else: #ch == 'E'
            digitArr = sorted(digitArr)
            result.append(digitArr.pop(0))
    return ','.join(result)
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print OffLineMinimum(["1","2","E","E","3"])  
