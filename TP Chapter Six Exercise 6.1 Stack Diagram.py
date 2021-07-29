# Stack Diagram takin' ova 4 da 99 and the 2000!

'''
Draw a stack diagram for the following program. What does the program print?
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square


x = 1
y = x + 1
print(c(x, y+3, x+y))


def b(z):

    prod = a times z, z times
    prints z and the prod == a * z
    returns the value of prod (a * z)

def a(x, y):

    x's value becomes x plus 1
    return x raised by 1 each time times y

def c(x, y, z):

    total's value becomes x, y and z added together
    square multiplies b times the value of total first, then squares it
    return is the value of square

x's value is 1

y's value is x + 1

prints (x = 1 as x, 1+1+3 as y, and x = 1 + x + 1 as z)
(x == 1, y == 5, z == 2 )

print c(1, 5, 2)

total = 1 + 5 + 2 = 8
square calls b so we gotta do this bullshit...

b calls z == 2

prod = a times z, z times...back to a, ugh

a(1, 5):
    x = 1 + 1, x == 2
    return 2 * 5 == 10

back to b...

prod = 10 * 2 = 20, z times so times 2 == 40

prints z which is 2 and prod which is 40

returns prod which is 40

back to printing c again

total = 8
square multiplies 40 times the value of 8 which is 320, then squared which is 102,400?
returns 102,400...I don't know about this...#MyGuy.
'''


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square


x = 1
y = x + 1
print(c(x, y + 3, x + y))

'''
Answer - https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex6/ex6.1.py

Exercise 6.1.
Draw a stack diagram for the following program. What does the program print?
    def b(z):
        prod = a(z, z)
        print(z, prod)
        return prod
    def a(x, y):
        x = x + 1
        return x * y
    def c(x, y, z):
        total = x + y + z
        square = b(total)**2
        return square
    x = 1
    y = x + 1
    print(c(x, y+3, x+y))
"""

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1  == 1 + 1 + 1 = 3 for x, x + 1 aso equals y so y = 3 too
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))


main:
    x ---> 1
    y ---> 2
c:
    x ---> 1
    y ---> 5
    z ---> 3
    total ---> 9
    square ---> 8100
b:
    z ---> 9
    prod ---> 90
a:
    x ---> 9
    y ---> 9
    x ---> 10

Program prints:
9 90
8100



