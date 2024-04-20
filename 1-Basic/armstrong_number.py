def findArmstrongNumber(num):
    num_str = str(num)
    n = len(num_str)
    temp = 0
    for digit in num_str:
        temp += int(digit) ** n
    if temp == num:
        return True
    else:
        return False
