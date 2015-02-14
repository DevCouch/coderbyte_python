def BinaryConverter(str):
    str = str[::-1]
    str_sum = 0
    power = 0
    for ch in str:
        str_sum += int(ch) * (2 ** power)
        power += 1
    return str_sum
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print BinaryConverter("001")  
print BinaryConverter("010")  
print BinaryConverter("011")  
print BinaryConverter("100") 
print BinaryConverter("100101")  
