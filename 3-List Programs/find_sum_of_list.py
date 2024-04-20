def findSum(arr):
    return sum(arr)


print(findSum([11, 12, 13, 14, 15]))


def withFor(arr):
    temp = 0
    for i in arr:
        temp += i
    return temp


print(withFor([11, 12, 13, 14, 15]))
