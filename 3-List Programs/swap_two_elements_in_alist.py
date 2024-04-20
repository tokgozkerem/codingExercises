def newlist(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


# print(newlist([10, 15, 20, 25], 1, 2))


def enumList(arr, pos1, pos2):
    for a, b in enumerate(arr):
        if a == pos1:
            arr[pos1] = arr[pos2]
        elif a == pos2:
            arr[pos2] = arr[pos1]
    return arr


# print(enumList([10, 15, 20, 25], 1, 3))
