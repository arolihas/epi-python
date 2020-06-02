def reverse(x):
    rev, rem = 0, abs(x)
    while rem:
        rev = (rev * 10) + rem % 10
        rem //= 10
    return -result if x < 0 else result
