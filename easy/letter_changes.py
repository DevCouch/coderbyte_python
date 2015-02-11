def LetterChanges(input): 
  vowels = 'aeiou'
  output = ''
  for ch in input: 
    ordNumber = ord(ch)
    if ordNumber >= 97 and ordNumber <= 122:
      ordNumber += 1
      if ordNumber == 123:
        ordNumber = 97
    ch = str(unichr(ordNumber))
    if ch in vowels:
      ch = ch.upper()
    output += ch  
  
  
  return output
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges("Marmalade")