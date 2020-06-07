def longest_equal_subarray(arr):
    longest, curr = 1, 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            curr += 1 
        else:
            curr = 1
        longest = max(longest, curr)
    return longest
