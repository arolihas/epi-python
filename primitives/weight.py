# Return closest int with the same number of 1s as x in bit representation
def weight(x): 
    ns = x & ~(x-1)
    s = ~x & (x+1)
    if ns > s:
        x |= ns
        x ^= (ns >> 1)
    else:
        x ^= s
        x |= (s >> 1)
    return x
