def random_sampling(it, k):
    results = list(itertools.islice(it, k))
    seen = k
    for x in it:
        seen += 1
        replace = random.randrange(seen)
        if replace < k:
            results[replace] = x
    return results
