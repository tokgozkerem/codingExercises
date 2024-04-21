def oddNums(arr):
    new_list = [num for num in arr if num % 2 != 0]
    return new_list


print(oddNums([11, 12, 13, 14, 15, 16, 17, 18]))


def odd(arr):
    odd_list = []
    for i in arr:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


print(odd([11, 12, 13, 14, 15, 16, 17, 18]))
