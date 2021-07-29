'''

p. 103

Chapter 11 - Dictionaries

p. 103 - 104 11. 1 A dictionary is a mapping

A dictionary is like a list, but more general. In a list, the indices have to be integers; in a
dictionary they can be (almost) any type.

A dictionary contains a collection of indices, which are called keys, and a collection of
values. Each key is associated with a single value. The association of a key and a value is
called a key-value pair or sometimes an item.

In mathematical language, a dictionary represents a mapping from keys to values, so you
can also say that each key “maps to” a value. As an example, we’ll build a dictionary that
maps from English to Spanish words, so the keys and the values are all strings.

The function dict creates a new dictionary with no items. Because dict is the name of a
built-in function, you should avoid using it as a variable name.

>>> eng2sp = dict()
>>> eng2sp
{}

The squiggly-brackets, {}, represent an empty dictionary. To add items to the dictionary,
you can use square brackets:

>>> eng2sp['one'] = 'uno'

This line creates an item that maps from the key 'one' to the value 'uno'. If we print the
dictionary again, we see a key-value pair with a colon between the key and value:

>>> eng2sp

{'one': 'uno'}

This output format is also an input format. For example, you can create a new dictionary
with three items:

104 Chapter 11. Dictionaries
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

But if you print eng2sp, you might be surprised:

>>> eng2sp
{'one': 'uno', 'three': 'tres', 'two': 'dos'}

The order of the key-value pairs might not be the same. If you type the same example
on your computer, you might get a different result. In general, the order of items in a
dictionary is unpredictable.

But that’s not a problem because the elements of a dictionary are never indexed with integer
indices. Instead, you use the keys to look up the corresponding values:

>>> eng2sp['two']

'dos'

The key 'two' always maps to the value 'dos' so the order of the items doesn’t matter.

If the key isn’t in the dictionary, you get an exception:
>>> eng2sp['four']
KeyError: 'four'

The len function works on dictionaries; it returns the number of key-value pairs:

>>> len(eng2sp)
3

The in operator works on dictionaries, too; it tells you whether something appears as a key
in the dictionary (appearing as a value is not good enough).

>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False

To see whether something appears as a value in a dictionary, you can use the method
values, which returns a collection of values, and then use the in operator:
>>> vals = eng2sp.values()
>>> 'uno' in vals
True

The in operator uses different algorithms for lists and dictionaries. For lists, it searches the
elements of the list in order, as in Section 8.6. As the list gets longer, the search time gets
longer in direct proportion.

Python dictionaries use a data structure called a hashtable that has a remarkable property:
the in operator takes about the same amount of time no matter how many items are in the
dictionary. I explain how that’s possible in Section B.4, but the explanation might not make
sense until you’ve read a few more chapters.

p. 104-106 11.2 Dictionary as a collection of counters

An implementation is a way of performing a computation; some implementations are
better than others. For example, an advantage of the dictionary implementation is that we
don’t have to know ahead of time which letters appear in the string and we only have to
make room for the letters that do appear.

Here is what the code might look like:
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


The name of the function is histogram, which is a statistical term for a collection of counters
(or frequencies).

The first line of the function creates an empty dictionary. The for loop traverses the string.
Each time through the loop, if the character c is not in the dictionary, we create a new item
with key c and the initial value 1 (since we have seen this letter once). If c is already in the
dictionary we increment d[c].

Here’s how it works:
>>> h = histogram('brontosaurus')
>>> h
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
The histogram indicates that the letters 'a' and 'b' appear once; 'o' appears twice, and
so on.

Dictionaries have a method called get that takes a key and a default value. If the key
appears in the dictionary, get returns the corresponding value; otherwise it returns the
default value. For example:

>>> h = histogram('a')
>>> h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('c', 0)
0

As an exercise, use get to write histogram more concisely. You should be able to eliminate
the if statement.



def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('aye')
print(h)

# the second argument 0 is the default value, basically asking if a is in the word in the
# first place
print(h.get('a', 0))
print(h.get('c', 0))

# Answer help - https://python-forum.io/Thread-how-do-i-use-get-for-my-histogram-function


def getagram(word):
    d = dict()
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    return d



You search through every letter in word and make it look for the key "letter" in the
dictionary. You use get with the default value of 0 to see if the letter's in the
dictionary in the first place. After that, the letter increases by 1 it appears in the
dictionary.



print(getagram('aye'))

p. 106 11.3 Looping and dictionaries

If you use a dictionary in a for statement, it traverses the keys of the dictionary. For example,
print_hist prints each key and the corresponding value:

def print_hist(h):
    for c in h:
        print(c, h[c])

Here’s what the output looks like:
>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1

Again, the keys are in no particular order. To traverse the keys in sorted order, you can use
the built-in function sorted:
>>> for key in sorted(h):
... print(key, h[key])
a 1
o 1
p 1
r 2
t 1

p. 106-107

Here is a function that takes a value and returns the first key that maps to that value:

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

This function is yet another example of the search pattern, but it uses a feature we haven’t
seen before, raise. The raise statement causes an exception; in this case it causes a
LookupError, which is a built-in exception used to indicate that a lookup operation failed.
If we get to the end of the loop, that means v doesn’t appear in the dictionary as a value, so
we raise an exception.

Here is an example of a successful reverse lookup:

>>> h = histogram('parrot')
>>> key = reverse_lookup(h, 2)
>>> key
'r'

And an unsuccessful one:
>>> key = reverse_lookup(h, 3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 5, in reverse_lookup
LookupError

The effect when you raise an exception is the same as when Python raises one: it prints a
traceback and an error message.

When you raise an exception, you can provide a detailed error message as an optional
argument. For example:

>>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary

A reverse lookup is much slower than a forward lookup; if you have to do it often, or if the
dictionary gets big, the performance of your program will suffer.

p. 107-108 11.5 Dictionaries and lists

Lists can appear as values in a dictionary. For example, if you are given a dictionary that
maps from letters to frequencies, you might want to invert it; that is, create a dictionary
that maps from frequencies to letters. Since there might be several letters with the same
frequency, each value in the inverted dictionary should be a list of letters.

Here is a function that inverts a dictionary:

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

Here is an example:
>>> hist = histogram('parrot')
>>> hist
{'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
>>> inverse = invert_dict(hist)
>>> inverse
{1: ['a', 'p', 't', 'o'], 2: ['r']}

Lists can be values in a dictionary, as this example shows, but they cannot be keys. Here’s
what happens if you try:
>>> t = [1, 2, 3]
>>> d = dict()
>>> d[t] = 'oops'
Traceback (most recent call last):
File "<stdin>", line 1, in ?
TypeError: list objects are unhashable
I mentioned earlier that a dictionary is implemented using a hashtable and that means that
the keys have to be hashable.

I mentioned earlier that a dictionary is implemented using a hashtable and that means that
the keys have to be hashable.

A hash is a function that takes a value (of any kind) and returns an integer. Dictionaries
use these integers, called hash values, to store and look up key-value pairs.

This system works fine if the keys are immutable. But if the keys are mutable, like lists,
bad things happen. For example, when you create a key-value pair, Python hashes the key
and stores it in the corresponding location. If you modify the key and then hash it again, it
would go to a different location. In that case you might have two entries for the same key,
or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.

That’s why keys have to be hashable, and why mutable types like lists aren’t. The simplest
way to get around this limitation is to use tuples, which we will see in the next chapter.

p. 109 11.6 Memos

If you played with the fibonacci function from Section 6.7, you might have noticed that
the bigger the argument you provide, the longer the function takes to run. Furthermore,
the run time increases quickly.

To understand why, consider Figure 11.2, which shows the call graph for fibonacci with
n=4:
'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(30))

'''
A call graph shows a set of function frames, with lines connecting each frame to the frames
of the functions it calls. At the top of the graph, fibonacci with n=4 calls fibonacci with
n=3 and n=2. In turn, fibonacci with n=3 calls fibonacci with n=2 and n=1. And so on.

Count how many times fibonacci(0) and fibonacci(1) are called. This is an inefficient
solution to the problem, and it gets worse as the argument gets bigger.

One solution is to keep track of values that have already been computed by storing them
in a dictionary. A previously computed value that is stored for later use is called a memo.
Here is a “memoized” version of fibonacci:

known = {0: 0, 1: 1}


def fibonasty(n):
    if n in known:
        return known[n]

    res = fibonasty(n - 1) + fibonasty(n - 2)
    known[n] = res
    return res


print(fibonasty(30))

known is a dictionary that keeps track of the Fibonacci numbers we already know. It starts
with two items: 0 maps to 0 and 1 maps to 1.

Whenever fibonacci is called, it checks known. If the result is already there, it can return
immediately. Otherwise it has to compute the new value, add it to the dictionary, and
return it.

If you run this version of fibonacci and compare it with the original, you will find that it
is much faster.

p. 110-111 11.7 Global variables

In the previous example, known is created outside the function, so it belongs to the special
frame called __main__. Variables in __main__ are sometimes called global because they
can be accessed from any function. Unlike local variables, which disappear when their
function ends, global variables persist from one function call to the next.

It is common to use global variables for flags; that is, boolean variables that indicate (“flag”)
whether a condition is true. For example, some programs use a flag named verbose to
control the level of detail in the output:
'''
verbose = True


def example1():
    if verbose:
        print('Running example1')


example1()
'''
If you try to reassign a global variable, you might be surprised. The following example is
supposed to keep track of whether the function has been called:
'''
been_called = False


def example2():
    been_called = True  # WRONG


example2()
print(been_called)
'''

But if you run it you will see that the value of been_called doesn’t change. The problem
is that example2 creates a new local variable named been_called. The local variable goes
away when the function ends, and has no effect on the global variable.

To reassign a global variable inside a function you have to declare the global variable
before you use it:
'''
been_called = False


def example2():
    global been_called
    been_called = True


'''
The global statement tells the interpreter something like, “In this function, when I say
been_called, I mean the global variable; don’t create a local one.”

Here’s an example that tries to update a global variable:
'''
count = 0


# def example3():
#   count = count + 1       # WRONG


# example3()
# print(count)
'''
If you run it you get:

UnboundLocalError: local variable 'count' referenced before assignment

Python assumes that count is local, and under that assumption you are reading it before
writing it. The solution, again, is to declare count global.
'''


def example3():
    global count
    count += 1


example3()      # run the function to make the function grab the global varial count and add 1
print(count)    # the global variabl count increased from 0 to 1
'''
If a global variable refers to a mutable value, you can modify the value without declaring
the variable:
'''
known = {0: 0, 1: 1}


def example4():
    known[2] = 1


example4()

# The variable refers to a dictionary which is mutable i.e. can be changed. Therefore, you
# can make a function that adds a key:value pair to a dictionary.

print(known)    # adds 2: 1 to the dictionary
'''
So you can add, remove and replace elements of a global list or dictionary, but if you want
to reassign the variable, you have to declare it:
'''


def example5():
    global known
    known = dict()


example5()

# The function reassigned the value to another blank dictionary. The REASSIGNMENT
# necessitates using global no matter what.

print(known)    # now known is an empty dictionary. I get it but this example was weird. =(
'''
Global variables can be useful, but if you have a lot of them, and you modify them frequently,
they can make programs hard to debug.

p. 111 11.8 Debugging

Scale down the input: If possible, reduce the size of the dataset. For example if the program
reads a text file, start with just the first 10 lines, or with the smallest example
you can find.

Check summaries and types: Instead of printing and checking the entire dataset, consider
printing summaries of the data: for example, the number of items in a dictionary or
the total of a list of numbers.
A common cause of runtime errors is a value that is not the right type. For debugging
this kind of error, it is often enough to print the type of a value.

Write self-checks: Sometimes you can write code to check for errors automatically. For
example, if you are computing the average of a list of numbers, you could check that
the result is not greater than the largest element in the list or less than the smallest.
This is called a “sanity check” because it detects results that are “insane”.

Another kind of check compares the results of two different computations to see if
they are consistent. This is called a “consistency check”.
'''
