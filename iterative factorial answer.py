def getFactorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for x in range(1, n + 1):
            factorial = factorial * x
        return factorial


n = 5
print(getFactorial(n))
