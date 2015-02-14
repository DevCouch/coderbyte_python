def permutations_impl(iterable, count, arr):
    permutation_list = []
    i = 0
    orig_arr = arr[:]
    while i < len(iterable):
        arr.append(iterable[i])
        if (count > 1):
            new_arr = iterable[:]
            new_arr.remove(iterable[i])
            count -= 1
            permutation_list.extend(permutations_impl(new_arr, count, arr))
            count += 1
        else:
            permutation_list.append(arr)
        i += 1
        arr = orig_arr[:]
    return permutation_list

def permutations(iterable, count):
     return permutations_impl(iterable, count, [])
    
def ArrayAddition(arr): 
    max_elem = max(arr)
    arr.remove(max_elem)
    for i in range(1, len(arr) + 1):
        for l in permutations(arr[:], i):
            if sum(l) == max_elem:
                return "true"
    return "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArrayAddition([3,5,-1,8,12])  
print ArrayAddition([5,7,16,1,2])  
