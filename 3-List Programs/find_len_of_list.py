def findLen(arr):
    return len(arr)


# print(findLen([11, 12, 13, 14, 15]))


def find(arr):
    temp = 0
    for i in arr:
        temp = temp + 1
    return temp


# print(find([11, 12, 13, 14, 15]))


def withSum(arr):
    length = sum(1 for i in arr)
    return length


# print(withSum([11, 12, 13, 14, 15]))


def recursive(arr):
    if not arr:
        return 0
    return 1 + recursive(arr[1:])


print(recursive([11, 12, 13, 14, 15]))
