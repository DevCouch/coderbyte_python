def ThirdGreatest(strArr): 
    strArr.sort(lambda x,y: cmp(len(y), len(x)))
    return strArr[2]
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThirdGreatest(["one","two","three"])  
