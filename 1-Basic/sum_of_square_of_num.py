def sumSquare(num):
    sumN = 0
    for i in range(num + 1):
        sumN += i**2
    return sumN


# Another way
def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3

