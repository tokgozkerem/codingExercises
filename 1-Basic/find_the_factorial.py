def findFactorial(num):
    return 1 if (num == 1 or num == 0) else num * findFactorial(num - 1)


def factorial(num):
    temp = 1
    for i in range(2, num + 1):
        temp *= i
    return temp


import math


def fact(num):
    return math.factorial(num)
