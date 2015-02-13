def NumberAddition(str): 
    num_str = ""
    prev_is_num = False
    result = 0
    for ch in str:
        if ch.isdigit():
            num_str += ch
            prev_is_num = True
        elif prev_is_num:
            prev_is_num = False
            result += int(num_str)
            num_str = ""
    if num_str != "":
        result += int(num_str)
    return result
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print NumberAddition("10 2One Number*1*") 
