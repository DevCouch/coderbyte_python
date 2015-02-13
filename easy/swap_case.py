def SwapCase(str):
    result = ""
    for ch in str:
        if ch.isalpha():
            if ch.islower():
                result += ch.upper()
            else:
                result += ch.lower()
        else:
            result += ch
    return result
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SwapCase("Hello-LOL")  
