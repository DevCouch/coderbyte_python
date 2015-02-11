def FirstFactorial(num): 

  # code goes here
  factorial = 1
  counter = 1
  while counter <= num:
    factorial = factorial * counter
    counter += 1
  return factorial