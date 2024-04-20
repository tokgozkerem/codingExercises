def findMin(arr):
    return min(arr)


def findSortmin(arr):
    arr.sort()
    return arr[0]


print(findMin([1, 0, -3, 4, 15]))
