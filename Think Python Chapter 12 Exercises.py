'''

Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http:
// en. wikipedia. org/ wiki/ Letter_ frequencies .




def most_frequent(word):
    d = dict()
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    return d


print(most_frequent('SEATTLE SUP'))

Wrong - Answer below
https://github.com/AllenDowney/ThinkPython2/blob/master/code/most_frequent.py



def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.
    s: string
    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


string = read_file('emma.txt')
letter_seq = most_frequent(string)

for x in letter_seq:
    print(x)


Exercise 12.2. More anagrams!

1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.

Here is an example of what the output might look like:

['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a collection of letters to a list
of words that can be spelled with those letters. The question is, how can you represent the
collection of letters in a way that can be used as a key?

2. Modify the previous program so that it prints the longest list of anagrams first, followed by
the second longest, and so on.

3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What collection of 8 letters forms the most possible
bingos?



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


def is_anagram(x, y):
    return len(x) == len(y) and sorted(x) == sorted(y)


dictionary = make_dict("words.txt")



def make_dict(file):
    dictionary = dict()
    word_list = []
    fin = open(file)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary


def anagram_search(*args)
    options = []
    for words in word_list(*args):
        if len(args) == len(args) and sorted(args) == sorted(args):
            options.append(args)
    return options


print(anagram_search('words.txt'))

Wrong, answers below - https://github.com/AllenDowney/ThinkPython2/blob/master/code/anagram_sets.py




def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.
    d: map from words to list of their anagrams
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    """Select only the words in d that have n letters.
    d: map from word to list of anagrams
    n: integer number of letters
    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


anagram_map = all_anagrams('words.txt')
print_anagram_sets_in_order(anagram_map)

eight_letters = filter_length(anagram_map, 8)
print_anagram_sets_in_order(eight_letters)


Exercise 12.3. Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
swaps. Solution: http: // thinkpython2. com/ code/ metathesis. py . Credit: This exercise
is inspired by an example at http: // puzzlers. org .



def regular_word(b):
    return b


def all_methathasis(filename):
    """Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = regular_word(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

Wrong, answer below



import anagram_sets


def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.
    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Computes the number of differences between two words.
    word1, word2: strings
    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


sets = anagram_sets.all_anagrams('words.txt')
metathesis_pairs(sets)

Exercise 12.4. Here’s another Car Talk Puzzler (http: // www. cartalk. com/ content/
puzzlers ):

What is the longest English word, that remains a valid English word, as you remove its
letters one at a time?

Now, letters can be removed from either end, or the middle, but you can’t rearrange any
of the letters. Every time you drop a letter, you wind up with another English word. If
you do that, you’re eventually going to wind up with one letter and that too is going
to be an English word—one that’s found in the dictionary. I want to know what’s the
longest word and how many letters does it have?

I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
you take a letter off, one from the interior of the word, take the r away, and we’re left
with the word spite, then we take the e off the end, we’re left with spit, we take the s off,
we’re left with pit, it, and I.

Write a program to find all words that can be reduced in this way, and then find the longest one.
This exercise is a little more challenging than most, so here are some suggestions:

1. You might want to write a function that takes a word and computes a list of all the words that
can be formed by removing one letter. These are the “children” of the word.

2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can
consider the empty string reducible.

3. The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want
to add “I”, “a”, and the empty string.

4. To improve the performance of your program, you might want to memoize the words that are
known to be reducible.

Solution: http://thinkpython2.com/code/reducible.py .

read through answer
'''


def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d


"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    """If word is reducible, returns a list of its reducible children.
    Also adds an entry to the memo dictionary.
    A string is reducible if it has at least one child that is
    reducible.  The empty string is also reducible.
    word: string
    word_dict: dictionary with words as keys
    """
    # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    """Returns a list of all words that can be formed by removing one letter.
    word: string
    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i + 1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.
    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.
    If there is more than one choice, it chooses the first.
    word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them.
    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


word_dict = make_word_dict()
print_longest_words(word_dict)
