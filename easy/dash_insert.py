def DashInsert(str): 
    result = ""
    prev = 2
    for ch in str:
        if prev % 2 != 0 and int(ch) % 2 != 0:
            result += "-"
        result += ch
        prev = int(ch)
    return result 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print DashInsert("99946")  
