def fibonacciNum(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacciNum(num - 1) + fibonacciNum(num - 2)
