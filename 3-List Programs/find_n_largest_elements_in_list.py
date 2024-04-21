def findNlargest(arr, n):
    newlist = []
    for i in range(0, n):
        max1 = 0
        for j in range(len(arr)):
            if arr[j] > max1:
                max1 = arr[j]
        arr.remove(max1)
        newlist.append(max1)

    return newlist


# print(findNlargest([25, 36, 23, 11, 98], 2))
