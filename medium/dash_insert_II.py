def DashInsertII(num): 
    result = ""
    prev = 0
    for ch in str(num):
        if prev > 0 and int(ch) > 0:
            if prev % 2 != 0 and int(ch) % 2 != 0:
                result += "-"
            elif prev % 2 == 0 and int(ch) % 2 == 0:
                result += "*"
        result += ch
        prev = int(ch)
    return result 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print DashInsertII(10120) 
