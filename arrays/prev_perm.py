def previous_permutation(perm):
    inv = len(perm) - 2
    while (inv > -1 and perm[inv] <= perm[inv + 1]):
        inv -= 1
    if inv == -1:
        return []

    for i in range(len(perm) - 1, inv, -1):
        if perm[i] < perm[inv]:
            perm[i], perm[inv] = perm[inv], perm[i]
            break

    perm[inv + 1:] = reversed(perm[inv + 1:])
    return perm
