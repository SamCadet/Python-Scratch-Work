'''

p. 89 10.1 A list is a sequence

Like a string, a list is a sequence of values. In a string, the values are characters; in a list,
they can be any type. The values in a list are called elements or sometimes items.

There are several ways to create a new list; the simplest is to enclose the elements in square
brackets ([ and ]):

[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']

The elements of a list don’t have to be the same type.

['spam', 2.0, 5, [10, 20]]

A list within another list is nested.

As you might expect, you can assign list values to variables:

>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [42, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [42, 123] []

p. 90 10.2 Lists are mutable


The syntax for accessing the elements of a list is the same as for accessing the characters
of a string—the bracket operator. The expression inside the brackets specifies the index.
Remember that the indices start at 0:

>>> cheeses[0]
'Cheddar'

Unlike strings, lists are mutable. When the bracket operator appears on the left side of an
assignment, it identifies the element of the list that will be assigned.

>>> numbers = [42, 123]
>>> numbers[1] = 5
>>> numbers
[42, 5]


List indices work the same way as string indices:
• Any integer expression can be used as an index.
• If you try to read or write an element that does not exist, you get an IndexError.
• If an index has a negative value, it counts backward from the end of the list.
The in operator also works on lists.

>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False

p. 91 Traversing a list

The most common way to traverse the elements of a list is with a for loop. The syntax is
the same as for strings:

for cheese in cheeses:
    print(cheese)


This works well if you only need to read the elements of the list. But if you want to write
or update the elements, you need the indices. A common way to do that is to combine the
built-in functions range and len:

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

This loop traverses the list and updates each element. len returns the number of elements
in the list. range returns a list of indices from 0 to n 􀀀 1, where n is the length of the list.
Each time through the loop i gets the index of the next element. The assignment statement
in the body uses i to read the old value of the element and to assign the new value.


Although a list can contain another list, the nested list still counts as a single element. The
length of this list is four:

['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

p. 91 10.4 List operations

The + operator concatenates lists:
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> c
[1, 2, 3, 4, 5, 6]

The * operator repeats a list a given number of times:
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

The first example repeats [0] four times. The second example repeats the list [1, 2, 3]
three times.

p. 91 10.5 List slices

The slice operator also works on lists:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']

If you omit the first index, the slice starts at the beginning. If you omit the second, the slice
goes to the end. So if you omit both, the slice is a copy of the whole list.
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']

Since lists are mutable, it is often useful to make a copy before performing operations that
modify lists.

A slice operator on the left side of an assignment can update multiple elements:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> t
['a', 'x', 'y', 'd', 'e', 'f']

p. 92 List methods

>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> t
['a', 'b', 'c', 'd']

extend takes a list as an argument and appends all of the elements:

>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> t1
['a', 'b', 'c', 'd', 'e']

This example leaves t2 unmodified.
sort arranges the elements of the list from low to high:

>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> t
['a', 'b', 'c', 'd', 'e']

Most list methods are void; they modify the list and return None. If you accidentally write
t = t.sort(), you will be disappointed with the result.

t = ['d', 'c', 'e', 'b', 'a']
t = t.sort()

print(t)

It returns None. =(

p. 93-94 10.7 Map, filter and reduce
To add up all the numbers in a list, you can use a loop like this:

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

total is initialized to 0. Each time through the loop, x gets one element from the list.
The += operator provides a short way to update a variable. This augmented assignment
statement,

total += x

is equivalent to

total = total + x

As the loop runs, total accumulates the sum of the elements; a variable used this way is
sometimes called an accumulator.

Adding up the elements of a list is such a common operation that Python provides it as a
built-in function, sum:

t = [2, 5, 6]
# Answer should be 13 since it just adds all the numbers in the list
print(sum(t))

An operation like this that combines a sequence of elements into a single value is sometimes
called reduce.

Sometimes you want to traverse one list while building another. For example, the following
function takes a list of strings and returns a new list that contains capitalized strings:
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

res is initialized with an empty list; each time through the loop, we append the next element.
So res is another kind of accumulator.

An operation like capitalize_all is sometimes called a map because it “maps” a function
(in this case the method capitalize) onto each of the elements in a sequence.

Another common operation is to select some of the elements from a list and return a sublist.
For example, the following function takes a list of strings and returns a list that contains
only the uppercase strings:

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

isupper is a string method that returns True if the string contains only upper case letters.

An operation like only_upper is called a filter because it selects some of the elements and
filters out the others.

Most common list operations can be expressed as a combination of map, filter and reduce.

p. 94 10.8 Deleting elements

There are several ways to delete elements from a list. If you know the index of the element
you want, you can use pop:

t = ['ayo', 'myguy', 'whoadie']

x = t.pop(1)

print(t)
print(x)

pop modifies the list and returns the element that was removed. If you don’t provide an
index, it deletes and returns the last element.

If you don’t need the removed value, you can use the del operator:

t = ['ayo', 'myguy', 'whoadie']
del t[1]
print(t)

If you know the element you want to remove (but not the index), you can use remove:


t = ['ayo', 'myguy', 'whoadie']
t.remove('ayo')
print(t)

The return value from remove is None.

To remove more than one element, you can use del with a slice index:

t = ['ayo', 'myguy', 'whoadie', '#onhere', 'yerrrr', 'son']

del t[1:3]

print(t)

As usual, the slice selects all the elements up to but not including the second index.

p. 94-95

10.9 Lists and strings

A string is a sequence of characters and a list is a sequence of values, but a list of characters
is not the same as a string. To convert from a string to a list of characters, you can use list:

s = 'whoadie'

t = list(s)

print(t)

Because list is the name of a built-in function, you should avoid using it as a variable
name.

The list function breaks a string into individual letters. If you want to break a string into
words, you can use the split method:


s = 'I\'m doing my thing.'
t = s.split()
print(t)

An optional argument called a delimiter specifies which characters to use as word boundaries.
The following example uses a hyphen as a delimiter:


s = 'booty booty booty booty'
delimiter = '-'

t = s.split(delimiter)

print(t)

join is the inverse of split. It takes a list of strings and concatenates the elements. join is
a string method, so you have to invoke it on the delimiter and pass the list as a parameter:


t = ['Ayo,', 'pass', 'the', 'peas!']

delimiter = ' '

s = delimiter.join(t)

print(s)

In this case the delimiter is a space character, so join puts a space between words. To
concatenate strings without spaces, you can use the empty string, '', as a delimiter.

p. 95 10.10 Objects and values

To check whether two variables refer to the same object, you can use the is operator.

a = 'banana'

b = 'banana'

print(a is b)

In this example, Python only created one string object, and both a and b refer to it. But
when you create two lists, you get two objects:

a = [7, 8, 9]
b = [7, 8, 9]

print(a is b)
So the state diagram looks like Figure 10.3.

In this case we would say that the two lists are equivalent, because they have the same elements,
but not identical, because they are not the same object. If two objects are identical,
they are also equivalent, but if they are equivalent, they are not necessarily identical.

Until now, we have been using “object” and “value” interchangeably, but it is more precise
to say that an object has a value. If you evaluate [1, 2, 3], you get a list object whose
value is a sequence of integers. If another list has the same elements, we say it has the
same value, but it is not the same object.

p. 96-97 10.11 Aliasing

If a refers to an object and you assign b = a, then both variables refer to the same object:

a = [7, 8, 9]
b = a
print(b is a)

The state diagram looks like Figure 10.4.

The association of a variable with an object is called a reference. In this example, there are
two references to the same object.

An object with more than one reference has more than one name, so we say that the object
is aliased.

If the aliased object is mutable, changes made with one alias affect the other:

a = [7, 8, 9]
b = a

b[2] = 25

print(a)
[7, 8, 25]

Although this behavior can be useful, it is error-prone. In general, it is safer to avoid
aliasing when you are working with mutable objects.

For immutable objects like strings, aliasing is not as much of a problem. In this example:

a = 'banana'
b = 'banana'

It almost never makes a difference whether a and b refer to the same string or not.

p. 97-98 10.12 List arguments

When you pass a list to a function, the function gets a reference to the list. If the function
modifies the list, the caller sees the change. For example, delete_head removes the first
element from a list:

def delete_head(t):
    del t[0]

Here’s how it is used:

letters = ['a', 'b', 'c']
delete_head(letters)
letters
['b', 'c']

The parameter t and the variable letters are aliases for the same object. The stack diagram
looks like Figure 10.5.

It is important to distinguish between operations that modify lists and operations that create
new lists. For example, the append method modifies a list, but the + operator creates a
new list.

Here’s an example using append:

t1 = [1, 2]
t2 = t1.append(3)
t1
[1, 2, 3]
print(t2)
None

The return value from append is None.

Here’s an example using the + operator:

t1 = [5, 6]
t2 = t1.append(3)
print(t1)
[5, 6, 3]
t3 = t1 + [8]
print(t1)
[5, 6, 3]
print(t3)
[5, 6, 3, 8]

The result of the operator is a new list, and the original list is unchanged.

This difference is important when you write functions that are supposed to modify lists.
For example, this function does not delete the head of a list:

def bad_delete_head(t):
    t = t[1:]               # WRONG!

The slice operator creates a new list and the assignment makes t refer to it, but that doesn’t
affect the caller.



def bad_delete_head(t):
    t = t[1:]


t4 = [5, 6, 7]
bad_delete_head(t4)
print(t4)
[5, 6, 7]

At the beginning of bad_delete_head, t and t4 refer to the same list. At the end, t refers
to a new list, but t4 still refers to the original, unmodified list.

An alternative is to write a function that creates and returns a new list. For example, tail
returns all but the first element of a list:



def tail(t):
    return t[1:]



This function leaves the original list unmodified. Here’s how it is used:

letters = ['a', 'b', 'c']

rest = tail(letters)

print(rest)

p. 98-99 10.13 Debugging

1. Most list methods modify the argument and return None. This is the opposite of the
string methods, which return a new string and leave the original alone.
If you are used to writing string code like this:

word = word.strip()

It is tempting to write list code like this:

t = t.sort() # WRONG!

Because sort returns None, the next operation you perform with t is likely to fail.
Before using list methods and operators, you should read the documentation carefully
and then test them in interactive mode.

2. Pick an idiom and stick with it.

Part of the problem with lists is that there are too many ways to do things. For example,
to remove an element from a list, you can use pop, remove, del, or even a slice
assignment.

To add an element, you can use the append method or the + operator. Assuming that
t is a list and x is a list element, these are correct:

t.append(x)
t = t + [x]
t += [x]

And these are wrong:
t.append([x]) # WRONG!
t = t.append(x) # WRONG!
t + [x] # WRONG!
t = t + x # WRONG!

Try out each of these examples in interactive mode to make sure you understand
what they do. Notice that only the last one causes a runtime error; the other three are
legal, but they do the wrong thing.


t = [1, 4, 'woah', 'hey now']

t.append(5)
print(t)
t = t + ['my guy']
print(t)
t += ['whoadie']
print(t)

# adds a list [huh] within the list t instead of just adding to t
# t.append(['huh'])
# print(t)

# t = t.append('what')

# returns None because the return value from append is none, you have to make a new list with a new variable
# like this u = t + ['what'] to create the new list you intended.
# u = t + [8]

# print(u)
# prints [1, 4, 'woah', 'hey now', 5, 'my guy', 'whoadie', 8]

# t + ['yooo']
# print(t)
# You need to either use t = or another variable = to set this new variable for T

# t = t + x

# print(t)

# X isn't defined, it'd work if you assigned a value for x

3. Make copies to avoid aliasing.

If you want to use a method like sort that modifies the argument, but you need to
keep the original list as well, you can make a copy.

t = [41, 6, 9]

t2 = t[:]

t2.sort()

print(t)

# [41, 6, 9]

print(t2)

# [6, 9, 41]

In this example you could also use the built-in function sorted, which returns a new,
sorted list and leaves the original alone.

t = [41, 6, 9]

t2 = sorted(t)

print(t)

# [41, 6, 9]

print(t2)

# [6, 9, 41]
'''
