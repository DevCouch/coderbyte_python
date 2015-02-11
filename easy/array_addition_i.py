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
    
def test(arg):
    max_elem = max(arg)
    arg.remove(max_elem)
    for i in range(1, len(arg) + 1):
        for l in permutations(arg[:], i):
            if sum(l) == max_elem:
                return "true"
    return "false"
    #return permutations(arg[:], 3)

print test([3,5,-1,8,12])
