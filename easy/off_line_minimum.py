def OffLineMinimum(strArr): 
    digitArr = []
    result = []
    for ch in strArr:
        if ch.isdigit():
            digitArr.append(int(ch))
        else: #ch == 'E'
            digitArr = sorted(digitArr)
            result.append(digitArr.pop(0))
    return result
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print OffLineMinimum(["4","E","1","E","2","E","3","E"])  
