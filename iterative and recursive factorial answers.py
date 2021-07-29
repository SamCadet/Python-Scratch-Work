def getIterativeFactorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for x in range(1, n + 1):
            factorial = factorial * x
        return factorial


def getRecursiveFactorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * getRecursiveFactorial(n - 1)


n = 6
print(getIterativeFactorial(n))
print(getRecursiveFactorial(n))

# https://tinyurl.com/y6rzc8e3

print(ord("A"))
# print(ord('b'))

# print(f'{10:04b}')

print(bin(10)[2:])
