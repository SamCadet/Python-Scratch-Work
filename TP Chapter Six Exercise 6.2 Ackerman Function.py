'''
Exercise 6.2. The Ackermann function

don't forget to add return after conditionals, #myguy
'''


def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))
print(ack(3, 3))

# Larger values than (3, 4) give a RecursionError
