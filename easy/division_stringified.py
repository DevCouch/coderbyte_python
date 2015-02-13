def DivisionStringified(num1,num2): 

  # code goes here
  result = int(round(float(num1) / float(num2)))
  result_str = str(result)[::-1]
  result_str = ','.join([result_str[i:i+3] for i in range(0, len(result_str), 3)])
  return result_str[::-1]
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print DivisionStringified(5, 2)  
