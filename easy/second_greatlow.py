def SecondGreatLow(arr): 

  # code goes here
  if len(arr) > 2:
  	  arr = set(arr)
  sorted_arr = sorted(arr)
  second_low = sorted_arr[1]
  second_high = sorted_arr[-2]
  return str(second_low) + " " + str(second_high)
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SecondGreatLow([2, 2, 7, 5, 10])
