'''

Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>>


t = [[1, 2], 3, 4, 5, 6]
print(sum(t[0]))





def nested_sum(t):
    newList = []
    for x in t:
        newList += x
        total = 0
        for x in newList:
            total += x
    return total


t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))



Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumulative
sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]



def datNewSum(t):
    newList = []
    for i in range(len(t) - 1):
        if t[0] == 1:
            pass
        else:
            newIndex = [ + 1 for i in t]
            t[newIndex] += newList
    return t

# Wrong, just refere to the answer here. https://github.com/AllenDowney/ThinkPython2/blob/master/code/list_exercises.py



def datNewSum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    """
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res


t = [1, 2, 3]

print(datNewSum(t))


Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]



def middle(t):
    t.pop(0)
    t.pop(-1)
    return t


t = [1, 2, 3, 4]
print(middle(t))


Answer from book
def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    """
    return t[1:-1]

Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]



def chop(t):
    t.pop(0)
    t.pop(-1)           # Remember, leaving no return value will return None


t = [1, 2, 3, 4]
print(chop(t))
print(t)

Answer from the book...

def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    """
    del t[0]
    del t[-1]

Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False



def is_sorted(t):
    u = t.sort()
    if u is t:
        return True
    else:
        return False


t = [1, 2, 3]

print(is_sorted(t))

wrong answer, use the right one below.



def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    """
    return t == sorted(t)


t = [1, 5, 3]

print(is_sorted(t))

Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.



def is_anagram(x, y):
    return len(x) == len(y) and sorted(x) == sorted(y)


print(is_anagram('rob', 'bro'))

Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.

Answer help - https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/



def has_duplicates(t):
    for numbers in t:
        if t.count(numbers) > 1:
            return True
    return False


t = [5, 1, 3, 1, 4]

print(has_duplicates(t))

Exercise 10.8. This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .

If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.


from random import randint


def birthdayMatch():
    for dates in range(23):
        sameDates = 0
        dates = randint(1, 365)
        if dates == dates:
            sameDates += 1
    print('There\'s a ' + str((sameDates / 23) * 100) +
          '% chance for a bithday match in your class.')


print(birthdayMatch())

Answer from book


import random


def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.
    t: list
    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.
    n: int
    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.
    num_students: how many students in the group
    num_samples: how many groups to simulate
    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


print(main())

Exercise 10.9. Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?

Answer help from - https://github.com/AllenDowney/ThinkPython2/blob/master/code/wordlist.py

import time


def wordsAppend():
    """Reads lines from a file and builds a list using append."""
    selection = []
    file = open('words.txt')
    for elements in file:
        word = elements.strip()
        selection.append(word)
    return selection


def wordsIdiom():
    """Reads lines from a file and builds a list using list +."""
    selection = []
    file = open('words.txt')
    for elements in file:
        word = elements.strip()
        selection = selection + [word]
    return selection



startTime = time.time()
t = wordsAppend()
elapsedTime = time.time() - startTime

print(len(t))
print(t[:10])
print(elapsedTime, 'seconds')

startTime = time.time()
t = wordsIdiom()
elapsedTime = time.time() - startTime

print(len(t))
print(t[:10])
print(elapsedTime, 'seconds')

# The second one takes longer because it's calculating every time it adds a word to the list maybe?
# The other just appends the word and moves on.

Exercise 10.10. To check whether a word is in the word list, you could use the in operator, but it
would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary
(the book, not the data structure). You start in the middle and check to see whether the word you are
looking for comes before the word in the middle of the list. If so, you search the first half of the list
the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
take about 17 steps to find the word or conclude that it’s not there.
Write a function called in_bisect that takes a sorted list and a target value and returns True if
the word is in the list and False if it’s not.

Or you could read the documentation of the bisect module and use that!

import bisect

words = ['ayo', 'bro', 'cousin', 'dude', 'easy', 'foh', 'geekin', 'heek']
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect(words, 'clank'))

Answer from book...again - https://github.com/AllenDowney/ThinkPython2/blob/master/code/inlist.py



def make_word_list():
    """Reads lines from a file and builds a list using append.
    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


word_list = make_word_list()

for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print(word, 'in list', in_bisect(word_list, word))

for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print(word, 'in list', in_bisect_cheat(word_list, word))

Exercise 10.11. Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list.
'''


def reversePair(x):
    for words in x:
        if words[::-1] in x:
            print(words + ' and ' + words[::-1] + ' are a reverse pair.')


thangs = ['orb', 'hey', 'bro', 'bad', 'yuck', 'dab']

print(reversePair(thangs))

'''

Answer from book - https://github.com/AllenDowney/ThinkPython2/blob/master/code/reverse_pair.py

from inlist import in_bisect, make_word_list


def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.
    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)


if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])

Exercise 10.12. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled”. Solution: http: //

thinkpython2. com/ code/ interlock. py . Credit: This exercise is inspired by an example at
http: // puzzlers. org .

1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?

I quit, here's the answer haha. https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex10/ex10.12.py
'''
import bisect


def word_list(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    return li


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word


def interlock(word_list):
    interlocking_words = []
    for word in word_list:
        if in_bisect_cheat(word_list, word[::2]) and in_bisect_cheat(word_list, word[1::2]):
            interlockers = (word[::2], word[1::2], word)
            interlocking_words.append(interlockers)
    return interlocking_words


def three_way_interlock(word_list):
    interlocking_words = []
    for word in word_list:
        if in_bisect_cheat(word_list, word[::3]) and in_bisect_cheat(word_list, word[1::3]) \
                and in_bisect_cheat(word_list, word[2::3]):
            interlockers = (word[::3], word[1::3], word[2::3], word)
            interlocking_words.append(interlockers)
    return interlocking_words


# Answer1:
li = word_list("words.txt")
print(interlock(li))
print()

# Answer2:
# print(three_way_interlock(li))
