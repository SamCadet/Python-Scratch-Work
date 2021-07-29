#! python 3

'''
Exercise 7.3. The mathematician Srinivasa Ramanujan found an infinite series that can be
used to generate a numerical approximation of 1/p:

Write a function called estimate_pi that uses this formula to compute and return an estimate
of pi. It should use a while loop to compute terms of the summation until the last term is
smaller than 1e-15 (which is Python notation for 10􀀀15). You can check the result by
comparing it to math.pi.

# Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/pi.py
'''

import math

# TODO: Write a function called estimate_pi to return an estimate of pi.


def estimate_pi():
    total = 0

    k = 0

    factor = (2 * math.sqrt(2) / 9801)

    # TODO: Use a while loop to compute terms of the summation until the last term is smaller than Le-15.

    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)    # remeber to use math.factorial after importing math
        den = math.factorial(k)**4 * 396**(4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 10**-15:
            break
        k += 1

    return 1 / total


print(estimate_pi())
