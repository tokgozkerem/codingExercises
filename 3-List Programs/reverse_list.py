def withReverse(arr):
    arr.reverse()
    return arr


print(withReverse([11, 12, 13, 14, 15]))


def withSlice(arr):
    new_arr = arr[::-1]
    return new_arr


print(withSlice([11, 12, 13, 14, 15]))
