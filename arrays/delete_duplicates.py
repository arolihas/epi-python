def delete_duplicates(arr):
    i = 0
    dup_index = 1 
    while dup_index < len(arr):
        if arr[i] == arr[dup_index]:
            arr[dup_index] == -1
        else:
            i += 1 
        dup_index += 1
    i = 0
    j = 1
    while i < len(arr):
        while (arr[j] == -1):
            j += 1
        arr[i] = arr[j]
        i = i + 1
    return i

def better_delete_duplicates(arr):
    if not arr:
        return 0
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[write_index - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index
