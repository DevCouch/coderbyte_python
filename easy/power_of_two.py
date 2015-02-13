def PowersofTwo(num): 
    is_poweroftwo = False
    curr = 2
    while curr <= num:
        if curr == num:
            is_poweroftwo = True
        curr = curr * 2
    return "true" if is_poweroftwo else "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
#print PowersofTwo(16)
#print PowersofTwo(22)
print PowersofTwo(22)
