'''
p. 113 11.10 Exercises

Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.

If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator
and the bisection search.



def lookup(search):
    table = dict()
    for words in search:
        file = open('words.txt')
        keys = table[words]
        values = table[words] + 1
    return words


print(lookup(''))
Wrong - Answer below
https: // github.com / MadCzarls / Think - Python - 2e - --my - solutions / blob / master / ex11 / ex11.1.py

'''


def make_dict(file_input):
    dictionary = dict()
    word_list = []

    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary


def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False


dictionary = make_dict("words.txt")
print(word_hunter('bike', dictionary))
print(word_hunter('bro', dictionary))
'''
Exercise 11.2. Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict



def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d



Answer - https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex11/ex11.2.py



def invert_dict2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        # it's inverted so values go first, add [] to put former keys in a listen within the dictionary
        inverse.setdefault(val, []).append(key)
    return inverse


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
inverse2 = invert_dict2(hist)
print(inverse)
print(inverse2)

Exercise 11.3. Memoize the Ackermann function from Exercise 6.2 and see if memoization
makes it possible to evaluate the function with bigger arguments. Hint: no.

Exercise 6.2 Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/ackermann.py


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(1, 1))

# Can't even get values to work with...

Author's attempt which I don't understand...

cache = {}


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m - 1, ackermann(m, n - 1))
        return cache[m, n]


print(ackermann(3, 4))
print(ackermann(3, 6))

Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates
that takes a list as a parameter and returns True if there is any object that appears more
than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.

10.7 Answer help - https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/



def has_duplicates(t):
    for numbers in t:
        if t.count(numbers) > 1:
            return True
    return False


known = {5: 5, 1: 1, 3: 3, 1: 1, 4: 4}


def has_duplicates2(d):
    return d == d.items()


t = [5, 1, 3, 1, 4]
u = {5: 5, 1: 1, 3: 3, 1: 1, 4: 4}

print(has_duplicates(t))
print(has_duplicates2(u))

Wrong answer but decent try, real answer below
https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex11/ex11.4.py



def has_duplicates3(li):
    dictionary = dict()
    for word in li:
        if word in dictionary:
            return True
        dictionary[word] = True
    return False


print(has_duplicates3(t))

Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the
other (see rotate_word in Exercise 8.5). Write a program that reads a wordlist and
finds all the rotate pairs.

Answer to 8.5 -  https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex8/ex8.5.py



def rotate_word(word, shift):
    """Uses Ceasar cypher to encrypt given word using given shift."""
    rotated_word = ''
    for letter in word:
        rotated_word += chr(ord(letter) + shift)
    return rotated_word


print(rotate_word('cheer', 7))
print(rotate_word('IBM', -1))


def findRotateWords(li):
    table = dict()
    for words in li:
        if words == rotate_word('cheer', 7):
            table[words] += 1
    return table


stuff = ['cheer', 'IBM', 'jolly', 'HAL']

# print(findRotateWords(stuff))

Wrong again, just use this answer
https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex11/ex11.5.py



def make_dict(file_input):
    dictionary = dict()
    word_list = []

    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary


def rotate_word(word, shift):
    """Uses Ceasar cypher to encrypt given word using given shift."""
    rotated_word = ''
    for letter in word:
        rotated_word += chr(ord(letter) + shift)
    return rotated_word


def rotate_pairs(word_dict):
    """Returns dictionary with pairs "word:list of tuples with rotated_word and shift"
    which can be generated by using function rotate_word on every word in word_dict
    and pairing it with returned rotated word it the latter is also found in word_dict.
    """

    pairs = {}
    for letter in range(1, 27):  # numbers of letters in alphabet
        for word in word_dict:
            if rotate_word(word, letter) in word_dict:
                if word in pairs:
                    pairs[word].append((rotate_word(word, letter), letter))
                else:
                    pairs[word] = [(rotate_word(word, letter), letter)]
    return pairs


dictionary = make_dict("words.txt")
print(rotate_pairs(dictionary))

Exercise 11.6. Here’s another Puzzler from Car Talk (http: // www. cartalk. com/ content/
puzzlers ):

This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable,
five-letter word recently that has the following unique property. When you remove the
first letter, the remaining letters form a homophone of the original word, that is a word
that sounds exactly the same. Replace the first letter, that is, put it back and remove
the second letter and the result is yet another homophone of the original word. And the
question is, what’s the word?

Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter
word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first
letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the
rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you
put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is
a real word, it’s just not a homophone of the other two words.
But there is, however, at least one word that Dan and we know of, which will yield two
homophones if you remove either of the first two letters to make two, new four-letter
words. The question is, what’s the word?

You can use the dictionary from Exercise 11.1 to check whether a string is in the word list.

To check whether two words are homophones, you can use the CMU Pronouncing Dictionary. You
can download it from http: // www. speech. cs. cmu. edu/ cgi-bin/ cmudict or from http:
// thinkpython2. com/ code/ c06d and you can also download http: // thinkpython2.
com/ code/ pronounce. py , which provides a function named read_dictionary that reads the
pronouncing dictionary and returns a Python dictionary that maps from each word to a string
that describes its primary pronunciation.



def make_dict(file_input):
    dictionary = dict()
    word_list = []

    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary


def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False


dictionary = make_dict("words.txt")
# print(word_hunter('bike', dictionary))
# print(word_hunter('station', dictionary))

word = (word_hunter('BRINK', dictionary))


def pronounciation(word, file):
    for line in file:
        word = line.strip()
        if len(word) - 1 == 4:
            newWord = word.pop(0)
            if word == newWord:
                thirdWord = word.pop(1)
                if thirdWord == word:
                    return thirdWord


file = open('c06d.txt')

print(pronounciation(word, file))


Call it in, nice try. Here's the answer

https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex11/ex11.6.py



def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.
    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".
    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False


def homophones(word_dict):
    li = []
    for word in word_dict:
        homophone1 = word[1::]
        homophone2 = word[0] + word[2:]

        if word_hunter(homophone1, word_dict) and word_hunter(homophone2, word_dict):
            if word_dict[word] == word_dict[homophone1] and word_dict[word] == word_dict[homophone2]:
                li.append(word)
    return li


dictionary = read_dictionary()
t = homophones(dictionary)  # all word in CMU Pronouncing Dictionary which fullfill the conditions


# finding words with length=5 ("He came upon a (...)five-letter word")
# that are in homophones list and in words.txt

def make_dict(file_input):
    dictionary = dict()
    word_list = []

    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary

word_list = make_dict("words.txt")


for word in t:
    if len(word) == 5 and word_hunter(word, word_list):
        print(word)

'''
