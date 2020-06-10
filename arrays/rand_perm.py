def random_permutation(n):
    permutation = list(range(n))
    for i in range(n):
        r = random.randint(i, len(permutation) - 1)
        permutation[r], permutation[i] = permutation[i], permutation[r]
    return permutation
