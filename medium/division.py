def Division(num1,num2): 
  lower = min(num1, num2)
  for i in range(lower, 1, -1):
      if (num1 % i) == 0 and (num2 % i) == 0:
          return i
  return 1
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print Division(8, 8)  
print Division(8, 4)  
print Division(7, 3)  

