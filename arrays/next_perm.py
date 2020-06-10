def next_permutation(perm):
    inversion_point = len(perm) - 2
    while (inversion_point > -1 and 
            perm[inversion_point] >= perm[inversion_point] + 1):
        inversion_point -= 1
    
    if inversion_point == -1:
        return []

    for i in range(len(perm) - 1, inversion_point, -1):
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break
    
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm
