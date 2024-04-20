def maxMethod(arr):
    return max(arr)


# print(maxMethod([1000, 1001, 1002, 1003, 1004, 1005]))


def naiveMethod(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > temp:
            temp = arr[i]
    return temp


# print(naiveMethod([1000, 1001, 1002, 1003, 1004, 1005]))


def sortMethod(arr):
    arr.sort()
    return arr[-1]


# print(sortMethod([1000, 1001, 1002, 1003, 1004, 1005]))
