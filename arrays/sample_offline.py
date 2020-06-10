def random_sampling(arr, k):
    for i in range(k):
        r = random.randint(i, len(arr) - 1)
        arr[i], arr[r] = arr[r], arr[i]

