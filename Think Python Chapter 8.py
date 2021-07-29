
'''

# Chapter 8 - Strings

A string is a sequence, which means it is an ordered collection of other values.

p. 71-72 8.1 A string is a sequence

A string is a sequence of characters. You can access the characters one at a time with the
bracket operator:

>>> fruit = 'banana'
>>> letter = fruit[1]

The expression in brackets is called an index. The index indicates which character in the
sequence you want (hence the name).

But you might not get what you expect:
>>> letter
'a'

for computer scientists, the
index is an offset from the beginning of the string, and the offset of the first letter is zero.
>>> letter = fruit[0]
>>> letter
'b'

As an index you can use an expression that contains variables and operators:
>>> i = 1
>>> fruit[i]
'a'
>>> fruit[i+1]
'n'

But the value of the index has to be an integer. Otherwise you get:
>>> letter = fruit[1.5]
TypeError: string indices must be integers


p. 72 8.2 len
len is a built-in function that returns the number of characters in a string:
>>> fruit = 'banana'
>>> len(fruit)
6

To get the last letter of a string, you might be tempted to try something like this:
>>> length = len(fruit)
>>> last = fruit[length]
IndexError: string index out of range

The reason for the IndexError is that there is no letter in 'banana' with the index 6. Since
we started counting at zero, the six letters are numbered 0 to 5. To get the last character,
you have to subtract 1 from length:

>>> last = fruit[length-1]
>>> last
'a'
Or you can use negative indices, which count backward from the end of the string. The
expression fruit[-1] yields the last letter, fruit[-2] yields the second to last, and so on.

p. 72-73 8.3 Traversal with a for loop

A lot of computations involve processing a string one character at a time. Often they start
at the beginning, select each character in turn, do something to it, and continue until the
end. This pattern of processing is called a traversal. One way to write a traversal is with a
while loop:

fruit = 'banana'

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

This loop traverses the string and displays each letter on a line by itself. The loop
condition is index < len(fruit), so when index is equal to the length of the string,
the condition is false, and the body of the loop doesn’t run. The last character accessed
is the one with the index len(fruit)-1, which is the last character in the string.

As an exercise, write a function that takes a string as an argument and displays the letters
backward, one per line.

Answer - https://stackoverflow.com/questions/3901340/python-write-a-function-that-takes-a-string-as-an-argument-and-displays-the-le


def backwardstring(string):

    # starts at last letter i.e. index[-1] instead of the first i.e. index[0]
    index = len(string) - 1

    while index >= 0:           # you can't go under 0 for an index because you'll get an index error
        letter = string[index]
        print(letter)
        index = index - 1       # decrease the index by one each iteration until you reach index 0


string = 'kojo'
backwardstring(string)          # prints the string backwards

Another way to write a traversal is with a for loop:

for letter in fruit:
    print(letter)

Each time through the loop, the next character in the string is assigned to the variable
letter. The loop continues until no characters are left.

answer - https://stackoverflow.com/questions/4239330/think-python-how-to-think-like-a-computer-scientist-excercise-8-4

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in ('O', 'Q'):            # if letter is O or Q in prefixes
        print(letter + 'u' + suffix)    # add u to said letters
    else:
        print(letter + suffix)          # prints everything else as is.


p. 73-74 8.4 String slices

A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

>>> s = 'Monty Python'
>>> s[0:5]
'Monty'
>>> s[6:12]
'Python'
The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth”
character, including the first but excluding the last.

If you omit the first index (before the colon), the slice starts at the beginning of the string.
If you omit the second index, the slice goes to the end of the string:

If the first index is greater than or equal to the second the result is an empty string, represented
by two quotation marks:
>>> fruit = 'banana'
>>> fruit[3:3]

An empty string contains no characters and has length 0, but other than that, it is the same
as any other string.

p. 74 8.5 Strings are immutable

strings are immutable, which means you can’t change an
existing string. The best you can do is create a new string that is a variation on the original

>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> new_greeting
'Jello, world!'
This example concatenates a new first letter onto a slice of greeting. It has no effect on the
original string.

p. 75-76 8.6 Searching

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


In a sense, find is the inverse of the [] operator. Instead of taking an index and extracting
the corresponding character, it takes a character and finds the index where that character
appears. If the character is not found, the function returns -1.

This is the first example we have seen of a return statement inside a loop. If word[index]
== letter, the function breaks out of the loop and returns immediately.

If the character doesn’t appear in the string, the program exits the loop normally and returns
-1.

This pattern of computation—traversing a sequence and returning when we find what we
are looking for—is called a search.

p. 8.7 Looping and counting

The following program counts the number of times the letter a appears in a string:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

This program demonstrates another pattern of computation called a counter. The variable
count is initialized to 0 and then incremented each time an a is found. When the loop exits,
count contains the result—the total number of a’s.

p. 75-76 8.8 String methods
Strings provide methods that perform a variety of useful operations. A method is similar
to a function—it takes arguments and returns a value—but the syntax is different. For
example, the method upper takes a string and returns a new string with all uppercase
letters.
Instead of the function syntax upper(word), it uses the method syntax word.upper().
>>> word = 'banana'
>>> new_word = word.upper()
>>> new_word
'BANANA'

This form of dot notation specifies the name of the method, upper, and the name of the
string to apply the method to, word. The empty parentheses indicate that this method
takes no arguments.

A method call is called an invocation; in this case, we would say that we are invoking
upper on word.

By default, find starts at the beginning of the string, but it can take a second argument, the
index where it should start:
>>> word.find('na', 3)
4

This is an example of an optional argument; find can also take a third argument, the index
where it should stop:

name = 'bob'
print(name.find('b', 1, 2))

This search fails because b does not appear in the index range from 1 to 2, not including 2.
Searching up to, but not including, the second index makes find consistent with the slice
operator.

p. 76-77 8.9 The in operator
The word in is a boolean operator that takes two strings and returns True if the first appears
as a substring in the second:

p. 77 8.10 String comparison
The relational operators work on strings. To see if two strings are equal:

if word == 'banana':
    print('All right, bananas.')

Other relational operations are useful for putting words in alphabetical order:
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

Python does not handle uppercase and lowercase letters the same way people do. All the
uppercase letters come before all the lowercase letters, so:

Your word, Pineapple, comes before banana.

A common way to address this problem is to convert strings to a standard format, such as
all lowercase, before performing the comparison.

p. 77-78 - 8.11 Debugging

This function tests if two words are the reverse of each other but there are two errors.

If we test this function with the words “pots” and “stop”, we expect the return value True,
but we get an IndexError:
>>> is_reverse('pots', 'stop')
...
File "reverse.py", line 15, in is_reverse
if word1[i] != word2[j]:
IndexError: string index out of range

For debugging this kind of error, my first move is to print the values of the indices immediately
before the line where the error appears.

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)

    while j > 0:
        print(i, j)                 # print here
        if word1[i] != word2[j]:
            return False
        i = i+1
    j = j-1

return True

Now when I run the program again, I get more information:

>>> is_reverse('pots', 'stop')
0 4
...
IndexError: string index out of range

The first time through the loop, the value of j is 4, which is out of range for the
string 'pots'. The index of the last character is 3, so the initial value for j should be
len(word2)-1.
If I fix that error and run the program again, I get:
>>> is_reverse('pots', 'stop')
0 3
1 2
2 1
True

Starting with this diagram, run the program on paper, changing the values of i and j
during each iteration. Find and fix the second error in this function.

# Answer - https://paigelearnscode.wordpress.com/2015/08/page/2/



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


print(is_reverse('dog', 'god'))
'''
