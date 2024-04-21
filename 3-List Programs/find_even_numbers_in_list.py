def findEven(arr):
    new_list = [x for x in arr if x % 2 == 0]
    return new_list


print(findEven([11, 12, 13, 14, 15, 16, 17, 18]))


def even(arr):
    new_list = []
    for i in arr:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


print(even([11, 12, 13, 14, 15, 16, 17, 18]))
