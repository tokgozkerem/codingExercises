def cubesum(num):
    temp = 0
    for i in range(num + 1):
        temp += i**3
    return temp


print(cubesum(7))
