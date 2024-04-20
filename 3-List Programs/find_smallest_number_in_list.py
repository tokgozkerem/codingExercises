def smallestNum(arr):
    return min(arr)


# print(smallestNum([11, 12, 13, 14, 15]))


def findWithSort(arr):
    arr.sort()
    return arr[0]


# print(findWithSort([16, 11, 12, 13, 14, 15]))


def naive(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < temp:
            temp = arr[i]
    return temp


# print(naive([102, 1232, 133, 14, 15]))
