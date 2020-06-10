def nonuniform_generation(values, probabilities):
    prefix_sum = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix, random.random())
    return values[interval_idx]
