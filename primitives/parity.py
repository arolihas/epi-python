def parity(x):
    n = 64
    while n != 1:
        n /= 2
        x ^= (x >> n)
    return x & 0x1
