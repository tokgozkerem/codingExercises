def change(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


# print(change([10, 15, 20, 25]))


def interchange(arr):
    temp = arr[0]
    length = len(arr)
    arr[0] = arr[length - 1]
    arr[length - 1] = temp
    return arr


# print(interchange([10, 15, 20, 25]))
