def even_odd(arr):
    next_even, next_odd = 0, len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else: 
            next_even, next_odd = next_odd, next_even
            next_odd -= 1
