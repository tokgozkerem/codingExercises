def findMax(arr):
    return max(arr)


# print(findMax([10, 20, 30, 40]))


def findMaxSort(arr):
    n = len(arr)
    arr.sort()
    return arr[n - 1]


# print(findMaxSort([10, 20, 30, 40]))


def findLargest(arr):
    n = len(arr)
    larg = arr[0]
    for i in range(1, n):
        if arr[i] > larg:
            larg = arr[i]
    return larg


# print(findLargest([10, 20, 30, 40]))
