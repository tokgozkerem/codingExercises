def negativenums(arr):
    new_list = [num for num in arr if num < 0]
    return new_list


print(negativenums([-2, -5, 19, 45, -23, 0, 13]))


def negNums(arr):
    negatives = []
    for i in arr:
        if i < 0:
            negatives.append(i)
    return negatives


print(negNums([-2, -5, 19, 45, -23, 0, 13]))
