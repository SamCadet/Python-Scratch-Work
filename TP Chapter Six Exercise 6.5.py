'''
Exercise 6.5. The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder
when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.

don't forget to add return after conditionals, #myguy

Answer - https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python


def gcd(a, b):
    r = a % b
    if b == 0:
        return 0
    elif r == 0:
        print('This is it, WHAT?!')
'''


def gcd(a, b):
    if b == 0:
        return 0
    while b:
        a, b = b, a % b
    return a


print(gcd(20, 8))
print(gcd(21, 15))
print(gcd(40, 0))
