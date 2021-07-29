#! python 3

'''
palindrome.py - something dumb from Chapter 6, Exercise 6.3




def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


print(middle('aa'))
print(middle('a'))
print(middle(''))

# 1. Two letters don't return anything, one letter doesn't return anything and ''
# doesn't return anything either.

# 2. It's a Boolean so we can write it in to ways, either like so...


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# print(is_palindrome('bro'))

'''

# Or more concise...


def is_palindrome(word):
    print(word, word[::-1])
    return word == word[::-1]


print(is_palindrome('124536'))
print(is_palindrome('racecar'))
print(is_palindrome('noon'))
print(is_palindrome('redivider'))
print(is_palindrome('My Guy'))

# Alternative answer from the book but I like mine better. =)
# https://github.com/AllenDowney/ThinkPython2/blob/master/code/palindrome_soln.py
