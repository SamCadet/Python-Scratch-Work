'''

Exercise 9.7. This question is based on a Puzzler that was broadcast on the radio program Car
Talk (http: // www. cartalk. com/ content/ puzzlers ):

Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-
p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?

Write a program to find it. Solution: http: // thinkpython2. com/ code/ cartalk1. py.



# TODO: make a file object for words.txt

fin = open('words.txt')

# TODO: write a function that looks through words.txt to find words with three consecutive double letters.


def threeLetters(word):
    letter = 0
    while letter < len(word) - 1:
        if word[letter + 1] == word[letter]:
            return True
        letter = letter + 1
    return False


print(threeLetters('committee'))

My attempt was wrong.

Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/cartalk1.py



def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string
    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:  # if the previous letter is the same as the next letter
            count = count + 1       # add it to count
            if count == 3:          # if count hits three consecutive letters
                return True
            i = i + 2               # adds three letters to i
        else:
            i = i + 1 - 2 * count   # I think this makes the search keep looping until the end
            count = 0
    return False                    # return false for all other cases


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:                # for lines in file object
        word = line.strip()         # gets rid of \n
        # uses reduction to a previously solved problem by calling is_triple_double()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')

Exercise 9.8. Here’s another Car Talk Puzzler (http: // www. cartalk. com/ content/
puzzlers ):

“I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I’d see 3-0-0-0-0-0.

“Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
palindrome, so my odometer could have read 3-1-5-4-4-5.

“One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?”

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
these requirements. Solution: http: // thinkpython2. com/ code/ cartalk2. py .



# TODO: Reverse number using a loop


def number_palindrome(number):
    reverse = 0
    while(number != 0):
        r = number % 10
        reverse = reverse * 10 + r
        number = number / 10
    print(reverse)
# TODO: Start writing miles function


def miles_palindrome(miles):
    for x in range(100000, 999999):              # TODO: Get all six digit numbers
        if number_palindrome(miles) == miles:
            # TODO: print numbers that are palindromes from the last four numbers
            return True
            break
        else:
            return False

# TODO: print numbers that make the whole thing a palindrome


print(number_palindrome(23))
print(miles_palindrome(10))

Attempt was wrong, Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/cartalk2.py



def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start + length]
    return s[::-1] == s


def check(i):
    """Checks if the integer (i) has the desired properties.
    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i + 1, 1, 5) and
            has_palindrome(i + 2, 1, 4) and
            has_palindrome(i + 3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()

Exercise 9.9. Here’s another Car Talk Puzzler you can solve with a search (http: // www.
cartalk. com/ content/ puzzlers ):

“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.

“When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and
if we’re really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”

Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
method zfill useful. Z fill adds zeros to a string until it reaches the specified
length.





def ageSearch(num1, num2):
    for number in num1:
        if int(num1[::-1]) == int(num2):
            return True
        else:
            return False


print(ageSearch('234', '432'))

Attempt was wrong, Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/cartalk3.py

'''


def str_fill(i, n):
    """Returns i as a string with at least n digits.
    i: int
    n: int length
    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.
    i: int
    j: int
    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.
    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.
    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():
    """Finds age differences that satisfy the problem.
    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1


print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)
