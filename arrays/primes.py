def generate_primes(n):
    primes = []
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                sieve[i] = False
    return primes
