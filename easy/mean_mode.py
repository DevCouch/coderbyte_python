def MeanMode(arr): 

    # code goes here
    arr = sorted(arr)
    mean = sum(arr) / len(arr)
    mode = -1
    prev = -1
    count = -1
    max_count = -1
    for elem in arr:
        if max_count == -1:
            prev = elem
            count = 1
            max_count = 1
            mode = elem
        elif elem == prev:
            count += 1
        else:
            if count > max_count:
                max_count = count
                mode = prev
            count = 1
            prev = elem
    return 1 if mode == mean else 0
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MeanMode([5, 3, 3, 3, 1])
print MeanMode([1, 2, 3])
print MeanMode([10, 10])
