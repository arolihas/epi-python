def random_subset(n, k):
    changed_elements = {}
    for i in range(k):
        rand_idx = random.randrange(i, n)
        rand_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_mapped
    return changed_elements[:k]
    
