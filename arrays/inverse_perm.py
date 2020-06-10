# the array is also the permutation, apply it to itself in constant space
def inverse_permutation(arr):
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        new_arr[arr[i]] = i
    return new_arr
