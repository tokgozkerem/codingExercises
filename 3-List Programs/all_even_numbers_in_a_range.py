def evenums(start, end):
    even_list = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(evenums(1, 14))


def even(start, end):
    even = [num for num in range(start, end + 1) if num % 2 == 0]
    return even


print(even(1, 14))
