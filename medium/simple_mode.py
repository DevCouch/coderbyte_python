def SimpleMode(arr): 
    elem_set = {}
    for elem in arr:
        if elem not in elem_set:
            elem_set[elem] = 1
        else:
            elem_set[elem] = elem_set[elem] + 1
    mode = -1
    count = -1
    for key in elem_set.keys():
        if elem_set[key] > 1 and count < elem_set[key]:
            count = elem_set[key]
            mode = key
    return mode
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleMode([5,5,2,2,1])  
print SimpleMode([3,4,1,6,10])
print SimpleMode([100,200,100,45,3])
