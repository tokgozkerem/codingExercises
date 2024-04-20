def checkEl(arr, a):
    if a in arr:
        return True
    return False


# print(checkEl(arr=[1, 2, 3, 4, 5, 6], a=3))


def usingLoop(arr, a):
    for i in arr:
        if i == a:
            return True
    return False


# print(usingLoop(arr=[1, 2, 3, 4, 5, 6], a=13))


def usingCount(arr, a):
    return arr.count(a) > 0


# print(usingCount(arr=[1, 2, 3, 4, 5, 6], a=3))
