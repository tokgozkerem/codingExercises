def findPrime(start, end):
    primes = []
    for i in range(start, end):
        if i == 1 or i == 0:
            continue
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


print(findPrime(10, 19))
