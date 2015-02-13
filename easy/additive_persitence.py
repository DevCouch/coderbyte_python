def AdditivePersistence(num): 
    persistence = 0
    finished = False
    new_num = 0
    if num < 10:
        return persistence
    while not finished:
        for ch in str(num):
            new_num += int(ch)
        num = new_num
        new_num = 0
        persistence += 1
        if num < 10:
            finished = True
    return persistence
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print AdditivePersistence(4) 
