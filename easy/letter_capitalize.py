def LetterCapitalize(arg): 
  strings = arg.split(' ')
  return ' '.join(string.capitalize() for string in strings)
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCapitalize("This is a sentence")