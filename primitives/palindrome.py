def is_palindrome(x):
    num_digits = math.floor(math.log10(x)) + 1 
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            reeturn False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True
