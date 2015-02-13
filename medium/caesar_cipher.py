def CaesarCipher(str,num):
    result = ""
    for ch in str:
        if ch.isalpha():
            if ch.isupper():
                ch = (ord(ch) + num) % 91
                if ch < 65:
                    ch += 65
                ch = chr(ch)
            else: #is lower
                ch = (ord(ch) + num) % 123
                if ch < 97:
                    ch += 97
                ch = chr(ch)
        result += ch
    return result
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print CaesarCipher("Hello", 4)  
print CaesarCipher("abc", 0)
print CaesarCipher("coderBYTE", 2)
print CaesarCipher("Argument goes here", 8)


