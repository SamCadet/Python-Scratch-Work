'''
# Chapter 9 Case study: Word Play

p. 83-84 9.1 Reading word lists

The built-in function open takes the name of the file as a parameter and returns a
file object you can use to read the file.



fin = open('words.txt')


fin is a common name for a file object used for input. The file object provides several
methods for reading, including readline, which reads characters from the file until it gets
to a newline and returns the result as a string:


print(fin.readline())



The file object keeps track of where it is in the file, so if you call readline again, you get
the next word:


print(fin.readline())

if it’s the newline character that’s bothering you, we can get rid of it with the
string method strip: (Not necessary in Sublime Text but good to know anyway)
line = fin.readline()
word = line.strip()
word

You can also use a file object as part of a for loop. This program reads words.txt and
prints each word, one per line:

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)

p. 84 9.2 Exercises

Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
'''
# TODO: Make a variable for words.txt for the function

fin = open('words.txt')
'''
# TODO: Make the function that reads words.txt


def Words20(file):
    for x in file:
        line = fin.readline()
        if len(line) > 20:  # TODO: only print words that are more than 20 characters excluding whitespaces
            return line
        else:
            pass

# TODO: Call the function to test


print(Words20(fin))


Exercise 9.2.

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.

Write a program that reads words.txt and prints only the words that have no “e”. Compute the
percentage of words in the list that have no “e”.




def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True


print(has_no_e('fry'))

# make function  to check for e's in word.txt


def eCheck(file):
    for x in file:
        eFreeWords = 0
        eWords = 0
        line = fin.readline()
        while True:
            if 'e' not in line:  # if there are no e's in the word, return the line and add it to eFreeWords
                return line
                eFreeWords += 1
            else:
                eWords += 1  # otherwise, add it to eWords
                continue


print(eCheck(fin))

Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?


# make the function


def avoids(word):
    forbidden = 'j' or 'r' or 'v'
    if forbidden in word:
        return False
    else:
        return True


print(avoids('van'))


Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?



def uses_only(word):
    letters = 'a' and 'c' and 'e' and 'f' and 'h' and 'l' and 'o'
    if letters in word:
        return True
    else:
        return False


print(uses_only('ace'))


Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?

Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?


9.3 p. 85-87 Search
All of the exercises in the previous section have something in common;
they can be solved with the search pattern we saw in Section 8.6. The simplest example is:

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

The for loop traverses the characters in word. If we find the letter “e”, we can immediately
return False; otherwise we have to go to the next letter. If we exit the loop normally, that
means we didn’t find an “e”, so we return True.

You could write this function more concisely using the in operator, but I started with this
version because it demonstrates the logic of the search pattern.

avoids is a more general version of has_no_e but it has the same structure:

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

We can return False as soon as we find a forbidden letter; if we get to the end of the loop,
we return True.

uses_only is similar except that the sense of the condition is reversed:

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

Instead of a list of forbidden letters, we have a list of available letters. If we find a letter in
word that is not in available, we can return False.

uses_all is similar except that we reverse the role of the word and the string of letters:

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

Instead of traversing the letters in word, the loop traverses the required letters. If any of the
required letters do not appear in the word, we can return False.

If you were really thinking like a computer scientist, you would have recognized that
uses_all was an instance of a previously solved problem, and you would have written:

def uses_all(word, required):
    return uses_only(required, word)

This is an example of a program development plan called reduction to a previously solved
problem, which means that you recognize the problem you are working on as an instance
of a solved problem and apply an existing solution.

p. 86 9.4 Looping with indices

For is_abecedarian we have to compare adjacent letters, which is a little tricky with a for
loop:

def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

An alternative is to use recursion:

def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]
        return False
    return is_abecedarian(word[1:])

Another option is to use a while loop:



def is_abecedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i = i + 1
    return True

print(is_abecedarian('Flossy'))

The loop starts at i=0 and ends when i=len(word)-1. Each time through the loop, it compares
the ith character (which you can think of as the current character) to the i + 1th
character (which you can think of as the next).

If the next character is less than (alphabetically before) the current one, then we have discovered
a break in the abecedarian trend, and we return False.

If we get to the end of the loop without finding a fault, then the word passes the test. To
convince yourself that the loop ends correctly, consider an example like 'flossy'. The
length of the word is 6, so the last time the loop runs is when i is 4, which is the index of
the second-to-last character. On the last iteration, it compares the second-to-last character
to the last, which is what we want.

Here is a version of is_palindrome (see Exercise 6.3) that uses two indices; one starts at
the beginning and goes up; the other starts at the end and goes down.



def is_palindrome(word):
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True


print(is_palindrome('dad'))


# Or we could reduce to a previously solved problem and write:


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1

# Remember the lowest an index can go before it's out of range is 0.
# This while statement gets all of the letters from 0 upwards.
# Just saying j > 0 in the old code doesn't include 0.
# You could also say > -1 but 0 >= is clearer and more consistent with understanding how
# indexes include but can't go below 0 imo ofc.
    while j >= 0:
        print(i, j)                 # print here
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def is_palindrome(word):
    return is_reverse(word, word)


# Using is_reverse from Section 8.11.

print(is_palindrome('racecar'))

9.5 Debugging p. 87

Testing programs is hard. The functions in this chapter are relatively easy to test because
you can check the results by hand. Even so, it is somewhere between difficult and impossible
to choose a set of words that test for all possible errors.

Taking has_no_e as an example, there are two obvious cases to check: words that have an
‘e’ should return False, and words that don’t should return True. You should have no
trouble coming up with one of each.

Within each case, there are some less obvious subcases. Among the words that have an
“e”, you should test words with an “e” at the beginning, the end, and somewhere in the
middle. You should test long words, short words, and very short words, like the empty
string. The empty string is an example of a special case, which is one of the non-obvious
cases where errors often lurk.

In addition to the test cases you generate, you can also test your program with a word list
like words.txt. By scanning the output, you might be able to catch errors, but be careful:
you might catch one kind of error (words that should not be included, but are) and not
another (words that should be included, but aren’t).

In general, testing can help you find bugs, but it is not easy to generate a good set of
test cases, and even if you do, you can’t be sure your program is correct. According to a
legendary computer scientist:

Program testing can be used to show the presence of bugs, but never to show
their absence!
— Edsger W. Dijkstra
'''
