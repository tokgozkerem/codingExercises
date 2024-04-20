def multiply(arr):
    temp = 1
    for i in arr:
        temp = temp * i
    return temp


# print(multiply([11, 12, 13, 14, 15]))


def multiplyList(arr):
    temp = 1
    for i in range(0, len(arr)):
        temp = temp * arr[i]
    return temp


# print(multiplyList([11, 12, 13, 14, 15]))


def withListComp(arr):
    return 1 if not arr else arr[0] * withListComp(arr[1:])


# print(withListComp([11, 12, 13, 14, 15]))
