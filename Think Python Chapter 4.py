import turtle
import math

# p. 31 4.3


# 1. answer p. 32 4.4 Encapsulation

'''

bob = turtle.Turtle()
print(bob)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


square(bob) # This is encapsulation. You wrapped a piece of code
into a function to attach a name to it and re-use it below.

Randall = turtle.Turtle()
square(Randall) Now you can juse copy the function to call it

repeatedly instead of copying the whole code.

# 2 answer p. 32 4.5 Generalization

bob = turtle.Turtle()
print(bob)


def square(t, length): # Generalization like 'length' lets you add a parameter to a function to make it more general
    for i in range(4):
        t.fd(length)
        t.lt(90)


square(bob, 100)

# 3 answer p. 32 4.5 Generalization

bob = turtle.Turtle()
print(bob)


def polygon(t, n, length):  # t, n, and length are keyword arguments
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 7, 70)

'''

# 4 answer p. 33 4.6 Interface design
'''
bob = turtle.Turtle()
print(bob)


def polygon(t, n, length):  # t, n, and length are keyword arguments
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)


circle(bob, 90)


The interface of a function is a summary of how it is used: what are the parameters? What
does the function do? And what is the return value? An interface is “clean” if it allows the
caller to do what they want without dealing with unnecessary details.

In this example, r belongs in the interface because it specifies the circle to be drawn. n is
less appropriate because it pertains to the details of how the circle should be rendered.

'''

# 5 answer p. 34 Refactoring - rearranging a program to improve interfaces and facilitate code-reuse


bob = turtle.Turtle()
print(bob)


def polyline(t, n, length, angle):

'''Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.

You have to add polyline to avoid changing the interface for polygon.
'''
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


circle(bob, 40)
