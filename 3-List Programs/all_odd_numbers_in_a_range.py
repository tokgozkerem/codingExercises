def oddNums(start, end):
    oddNums = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            oddNums.append(i)

    return oddNums


# print(oddNums(1, 14))


def odd(start, end):
    odd_list = [num for num in range(start, end + 1) if num % 2 != 0]
    return odd_list


print(odd(1, 14))
