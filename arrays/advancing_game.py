# Move through an array by going as many spaces as A[i]
# Return if the end of the array can be reached starting from A[0]
def advancing_game(arr):
    i = 0
    furthest = arr[i]
    while furthest < len(arr) - 1 and i < len(arr) - 1:
        furthest = max(furthest, arr[i] + i)
        i += 1
    return furthest >= len(arr) - 1
