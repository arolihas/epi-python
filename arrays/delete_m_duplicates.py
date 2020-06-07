def delete_m_duplicates(arr, m):
    write_index = 1
    i = 0
    dup = min(m, 2)
    while i < len(arr) - dup:
        while arr[i] == arr[write_index]:
            write_index += 1
        if write_index > i + 1:
            arr[i + dup] = arr[write_index]
        i += 1
        if arr[i] > arr[write_index]:
            write_index = i + 1
    return arr
