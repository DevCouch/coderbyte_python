def PalindromeTwo(str): 
    new_str = ""
    for ch in str:
        if ch.isalpha():
            new_str += ch.lower()
    return "true" if new_str == new_str[::-1] else "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo("Noel - sees Leon")  
