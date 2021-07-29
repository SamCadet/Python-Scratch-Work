'''
p. 79-80 Exercises

Exercise 8.1. Read the documentation of the string methods at http: // docs. python. org/ 3/
library/ stdtypes. html# string-methods . You might want to experiment with some of them
to make sure you understand how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. For example, in
find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but
start is optional, and if you include start, then end is optional.

Exercise 8.2. There is a string method called count that is similar to the function in
Section 8.7. Read the documentation of this method and write an invocation that counts
the number of a’s in 'banana'.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

The syntax for PythonString Count()
Python count function syntax:

string.count(char or substring, start, end)

https://www.guru99.com/python-string-count.html

Parameters of Python Syntax
Char or substring: You can specify a single character or substring you are wants to search in
the given string. It will return you the count of the character or substring in the given
string.

start : (optional) It indicates the start index from where the search will begin. If not
given, it will start from 0. For example, you want to search for a character from the
middle of the string. You can give the start value to your count function.

end: (optional) It indicates the end index where the search ends. If not given, it will
search till the end of the list or string given. For example, you don't want to scan the
entire string and limit the search till a specific point you can give the value to end in
your count function, and the count will take care of searching till that point.


word = 'banana'
print(word.count('a'))


Exercise 8.3. A string slice can take a third index that specifies the “step size”; that is,
the number of spaces between successive characters. A step size of 2 means every other
character; 3 means every third, etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'

A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed
string. Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.

def is_palindrome(word):
    return word == word[::-1]


car = 'racecar'

print(car[::-1])

Exercise 8.4. The following functions are all intended to check whether a string contains
any lowercase letters, but at least some of them are wrong. For each function, describe
what the function actually does (assuming that the parameter is a string).



def any_lowercase1(s):              # sets definition
    for c in s:                     # for items in variable s
        if c.islower():             # if the all of the characters in the string are lowercased
            return True             # return true
        else:
            return False            # return false for all other cases


# this function is wrong because it's trying to see if any character's lower cased
# rather than all.
# word will only return true if every character is lower cased, one capitalized
# character makes it false.
word = 'yatunda'

print(any_lowercase1(word))


def any_lowercase2(s):              # sets definition
    for c in s:                     # for items in variable s
        if 'c'.islower():           # if everything in 'c' is lowercased, wrong
            return True             # return true
        else:
            return False

# This gets highjacked by 'c.islower()' since 'c' a lowercased string in itself. This will make
# anything you put in word true: even digits.


word = '45654'

print(any_lowercase2(word))


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# You give the variable a value of c.islower(). This won't work on
# strings with one capitalized letter.


word = 'heLlo'

print(any_lowercase3(word))


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# flag turns into an or statement.
# The or boolean becomes true when either statement is True or False. c.islower is True
# True or False always equals True so, once again, it doesn't matter what you put for word.
# This function will always be True.


word = 'hooty hoo'

print(any_lowercase4(word))


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True  # If every character in s isn't lowercase then return False, otherwise return True

# This code works


word = 'bASs'

print(any_lowercase5(word))


Exercise 8.5. A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.


# TODO: write a function that takes a string and integer as parameters


def rotate_word(string, integer):
    # TODO: use ord to rotate words by the integer amount.
    for letters in string:
        integer = 0
        letter = ord('0') + integer
    return letter


word = 'Hello'

print(rotate_word(word, 6))

Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/rotate.py
'''


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')        # Make start with 'A' since it's not 0 like 'a'
    elif letter.islower():
        start = ord('a')        # Make start with 'a' to establish 0
    else:
        return letter

    # Turns character into number and subtracts the value from 'a'
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)
# Takes value from see, moves it in places from the start, then divides by
# 26 since there are 26 letters to the alphabet and adds the upper or lower
# case start value.


# then returns (i) as a code to move the character down the alphabet n places
print(rotate_letter('d', 5))


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''                                # res is an empty string
    for letter in word:
        res += rotate_letter(letter, n)     # calls rotate_letter
    return res                              # applies it to the string in res


print(rotate_word('chonky', 7))
