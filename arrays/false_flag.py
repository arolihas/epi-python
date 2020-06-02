# Order array so all False's appear first
def false_flag(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        if not arr[start]:
            start += 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1

            # to maintain relative ordering have end=1 and then
            # increment to the next true for swaps

