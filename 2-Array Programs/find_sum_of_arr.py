def findSumArr(arr):
    return sum(arr)


# print(findSumArr([10, 20, 30, 40]))


def sumArr(arr):
    temp = 0
    for i in arr:
        temp += i
    return temp


# print(sumArr([10, 20, 30, 40]))


def enumerateArr(arr):
    temp = 0
    for i, a in enumerate(arr):  # i -> index
        # print(f"{i} index -> {a}")
        temp += a
    return temp


print(enumerateArr([10, 20, 30, 40]))
