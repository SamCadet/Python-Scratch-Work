import os
import ezsheets
import math

# p. 18 3.2

# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)
'''
radians = 0.7

height = math.sin(radians)


degrees = 45
radians = degrees / 180.0 * math.pi

print(math.sin(radians))

print(math.sqrt(2) / 2.0)

# p. 19 3.3

# the argument of a function can be any kind of expression, including arithmetic operators:
x = math.sin(degrees / 360.0 * 2 * math.pi)

# And even function calls:

x = math.exp(math.log(x + 1))



# p. 20-21 3.5


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# putting this before def print_lyrics gives the same output
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics() # calling this before it's defined creates a NameError

# p. 21-22 3.7


def print_twice(Whoadie):
    print(Whoadie)
    print(Whoadie)


print(print_twice('#MyGuy'))


p. 26 3.1




def right_justify(s):
    print('     ' * 14 + s)


right_justify('whoadie')



p. 27 3.2



# def print_spam():
#    print('spam')

# 1.

def print_spam():
    print('spam')

do_twice(print_spam)

# 2.


def do_twice(x, y):
    x(y)
    x(y)

# 3.


def print_twice(bruce):
    print(bruce)
    print(bruce)

# 4.


do_twice(print_twice, 'spam')

# 5.


def do_four(x, y):
    do_twice(x, y)
    do_twice(x, y)

do_four(print_twice, "whoadie")

# p. 27-28 Exercise 3.3

# My answer

def grid():
    print('+', ' ' * 5 + '+', ' ' * 5 + '+', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('+', ' ' * 5 + '+', ' ' * 5 + '+', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('|', ' ' * 5 + '|', ' ' * 5 + '|', end=' ')
    print('')
    print('+', ' ' * 5 + '+', ' ' * 5 + '+', end=' ')


grid()
'''

# Another one


def do_three(x):
    x()
    x()
    x()


def print_top():
    print('+----' + "+" + '----+', end='')
    print('')


def print_pillars():
    print('|    ' + '|' + '    |', end='')
    print('')


def area():
    print_top()
    print_pillars()


def print_grid():
    area()
    do_three(print_pillars)
    area()
    do_three(print_pillars)
    print_top()


print_grid()
