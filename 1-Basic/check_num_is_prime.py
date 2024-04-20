def checkPrime(num):
    for i in range(
        2, (num // 2) + 1):  # If a number has no divisors up to half of itself, then it is prime.
        if num % i == 0:
            return False
    return True
