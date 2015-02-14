def StringScramble(str1,str2):
    str1_arr = list(str1)
    for ch in str2:
        if ch in str1_arr:
            str1_arr.remove(ch)
        else:
            return "false"
    return "true"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble("cdore", "coder")  
print StringScramble("h3llko", "hello")  
