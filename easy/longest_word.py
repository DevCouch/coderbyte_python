def LongestWord(sen): 
  words = sen.split()
  correctedWords = []
  longestWord = ''
  for word in words:
    correctedWord = ''.join(e for e in word if e.isalnum())
    if len(correctedWord) > len(longestWord):
      longestWord = correctedWord
  return longestWord
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord("Which one is the longest word")