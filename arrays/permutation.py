def apply_permutation(arr, perm):
    perm_copy = perm[:]
    for i in range(len(arr)):
        while perm[i] > -1:
            p = perm[i]
            arr[i], arr[p] = arr[p], arr[i]
            perm[i] -= len(arr)
            i = p
    return arr

