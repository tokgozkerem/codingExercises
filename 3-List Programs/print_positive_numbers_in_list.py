def positiveNums(arr):
    positivenums = [num for num in arr if num >= 0]
    return positivenums


# print(positiveNums([-2, -5, 19, 45, -23, 0, 13]))


def posNums(arr):
    positive = []
    for i in arr:
        if i >= 0:
            positive.append(i)
    positive.sort()
    return positive


# print(posNums([-2, -5, 19, 45, -23, 0, 13]))
