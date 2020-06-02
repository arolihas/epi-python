def dutch_flag_partition(arr, i):
    pivot = arr[i]
    less, equal, more = 0, 0, len(arr) 
    while equal < more:
        if arr[equal] < pivot:
            arr[less], arr[equal] = arr[equal], arr[less]
            less += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            more -= 1
            arr[more], arr[equal] = arr[equal], arr[more]\

