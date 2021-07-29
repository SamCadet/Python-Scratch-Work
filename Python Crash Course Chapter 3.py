'''
Chapter 3 Introducing Lists

P. 33-34 What Is a List?

A list is a collection of items in a particular order. Because
a list usually contains more than one element, it’s a good idea to make the
name of your list plural, such as letters, digits, or names.


p. 34-35 Accessing Elements in a List

Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. To access an element
in a list, write the name of the list followed by the index of the item
enclosed in square brackets.

For example, let’s pull out the first bicycle in the list bicycles:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])

The syntax for this is shown at u. When we ask for a single item from a
list, Python returns just that element without square brackets:

trek

This is the result you want your users to see—clean, neatly formatted
output.

You can also use the string methods from Chapter 2 on any element
in this list. For example, you can format the element 'trek' more neatly by
using the title() method:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

This example produces the same output as the preceding example
except 'Trek' is capitalized.
'''
games = ['Zelda', 'NBA 2K', 'Mario', 'PGR']
# print(games[3].title())
print(games[3].upper())
'''
p. 35

Index Positions Start at 0, Not 1

Python considers the first item in a list to be at position 0, not position 1.
This is true of most programming languages, and the reason has to do with
how the list operations are implemented at a lower level. If you’re receiving
unexpected results, determine whether you are making a simple off-by-one
error.

Already know this stuff, just review...

Python has a special syntax for accessing the last element in a list. By asking
for the item at index -1, Python always returns the last item in the list:
'''
print(games[-1])
'''
This convention extends to other negative index values as well. The index -2 returns
the second item from the end of the list, the index -3 returns the third item from
the end, and so forth.

p. 35-36 Using Individual Values from a List

You can use individual values from a list just as you would any other variable.
For example, you can use f-strings to create a message based on a
value from a list.

Let’s try pulling the first bicycle from the list and composing a message
using that value.
'''
message = f"My favorite racing game series is {games[3].upper()}."
'''
At u, we build a sentence using the value at bicycles[0] and assign it to
the variable message. The output is a simple sentence about the first bicycle
in the list:
'''
print(message)
'''
My favorite racing game series is PGR.

p. 36 Changing, Adding, and Removing Elements

Modifying Elements in a List

The syntax for modifying an element is similar to the syntax for accessing
an element in a list. To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have.

For example, let’s say we have a list of motorcycles, and the first item in
the list is 'honda'. How would we change the value of this first item?

motorcycles.py u motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

v motorcycles[0] = 'ducati'
print(motorcycles)

The code at u defines the original list, with 'honda' as the first element.
The code at v changes the value of the first item to 'ducati'. The output
shows that the first item has indeed been changed, and the rest of the list
stays the same:
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']

You can change the value of any item in a list, not just the first item.


p. 37-38 Appending Elements to the End of a List

The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list. Using the same list we had in the previous example, we’ll add the
new element 'ducati' to the end of the list:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

u motorcycles.append('ducati')

print(motorcycles)

The append() method at u adds 'ducati' to the end of the list without
affecting any of the other elements in the list:
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']

The append() method makes it easy to build lists dynamically. For
example, you can start with an empty list and then add items to the list
using a series of append() calls. Using an empty list, let’s add the elements
'honda', 'yamaha', and 'suzuki' to the list:

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

The resulting list looks exactly the same as the lists in the previous
examples:

['honda', 'yamaha', 'suzuki']

Building lists this way is very common, because you often won’t know
the data your users want to store in a program until after the program is
running. To put your users in control, start by defining an empty list that
will hold the users’ values. Then append each new value provided to the list
you just created.

p. 38 Inserting Elements into a List

You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item.
motorcycles = ['honda', 'yamaha', 'suzuki']
u motorcycles.insert(0, 'ducati')
print(motorcycles)

In this example, the code at u inserts the value 'ducati' at the beginning
of the list. The insert() method opens a space at position 0 and stores
the value 'ducati' at that location. This operation shifts every other value
in the list one position to the right:

['ducati', 'honda', 'yamaha', 'suzuki']
'''
games.insert(0, 'Street Fighter')
print(games)
'''
p. 38 Removing Elements from a List
Just examples of why you'd remove items from a list

p. 39 Removing an Item Using the del Statement

If you know the position of the item you want to remove from a list, you can
use the del statement.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

The code at u uses del to remove the first item, 'honda', from the list of
motorcycles:
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']

You can remove an item from any position in a list using the del statement
if you know its index. For example, here’s how to remove the second
item, 'yamaha', in the list:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

The second motorcycle is deleted from the list:
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']

In both examples, you can no longer access the value that was removed
from the list after the del statement is used.
'''
print(games)
del games[2]
print(games)
'''
p. 39

Removing an Item Using the pop() Method

The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list.

Know this already...
'''
poppedGames = games.pop()
print(games)
print(poppedGames)
'''
The output shows that the value 'PGR' was removed from the end of
the list and is now assigned to the variable poppedGames:

PGR


How might this pop() method be useful? Imagine that the motorcycles
in the list are stored in chronological order according to when we owned
them. If this is the case, we can use the pop() method to print a statement
about the last motorcycle we bought:

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}.")

The output is a simple sentence about the most recent motorcycle we
owned:

The last motorcycle I owned was a Suzuki.

p. 4041 Popping Items from any Position in a List

You can use pop() to remove an item from any position in a list by including
the index of the item you want to remove in parentheses.
'''
nextGame = games.pop(2)
print(f'The next game I\'ll buy is {nextGame.title()}.')
'''
Remember that each time you use pop(), the item you work with is no
longer stored in the list.
If you’re unsure whether to use the del statement or the pop() method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method.

Removing an Item by Value

Sometimes you won’t know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, you
can use the remove() method.
'''

games = ['Zelda', 'NBA 2K', 'Mario', 'PGR']
print(games)
games.remove('NBA 2K')              # u
print(games)
'''
The code at u tells Python to figure out where 'ducati' appears in the
list and remove that element:

['Zelda', 'NBA 2K', 'Mario', 'PGR']
['Zelda', 'Mario', 'PGR']

You can also use the remove() method to work with a value that’s being
removed from a list. Let’s remove the value 'NBA 2K' and print a reason for
removing it from the list:
'''
games = ['Zelda', 'NBA 2K', 'Mario', 'PGR']                             # 1
print(games)

wack = 'NBA 2K'                                                         # 2
games.remove(wack)                                                      # 3
print(games)
print(f'\nI got rid of {wack.upper()} because it\'s weak as hell.')     # 4
'''
After defining the list at u, we assign the value 'NBA 2K' to a variable
called wack 2. We then use this variable to tell Python which value
to remove from the list at 3. At 4 the value 'NBA 2K' has been removed from
the list but is still accessible through the variable wack, allowing
us to print a statement about why we removed 'NBA 2K' from the list of
motorcycles:

The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed. You’ll learn how to do this in
Chapter 7.

p. 43 Organizing a List

Often, your lists will be created in an unpredictable order, because you can’t
always control the order in which your users provide their data. Although
this is unavoidable in most circumstances, you’ll frequently want to present
your information in a particular order. Sometimes you’ll want to preserve the
original order of your list, and other times you’ll want to change the original
order. Python provides a number of different ways to organize your lists,
depending on the situation.

p. 43-44 Sorting a List Permanently with the sort() Method

Python’s sort() method makes it relatively easy to sort

Python’s sort() method makes it relatively easy to sort a list. Imagine we
have a list of cars and want to change the order of the list to store them
alphabetically. To keep the task simple, let’s assume that all the values in
the list are lowercase.

cars.py cars = ['bmw', 'audi', 'toyota', 'subaru']
u cars.sort()
print(cars)

The sort() method, shown at u, changes the order of the list permanently.
The cars are now in alphabetical order, and we can never revert to
the original order:

['audi', 'bmw', 'subaru', 'toyota']

You can also sort this list in reverse alphabetical order by passing the
argument reverse=True to the sort() method. The following example sorts
the list of cars in reverse alphabetical order:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

Again, the order of the list is permanently changed:
['toyota', 'subaru', 'bmw', 'audi']
'''
print(games)
games.sort()
print(games)
games.sort(reverse=True)
print(games)
'''

p. 44-45 Sorting a List Temporarily with the sorted() Function

The sorted() function lets you display your list
in a particular order but doesn’t affect the actual order of the list.
'''
games = ['Zelda', 'NBA 2K', 'Mario', 'PGR']
print('Here\'s the original list:')
print(games)

print('Here\'s the sorted list:')
print(sorted(games))

print('Here\'s the original list again:')
print(games)
'''
Notice that the list still exists in its original order at x after the sorted()
function has been used. The sorted() function can also accept a reverse=True
argument if you want to display a list in reverse alphabetical order.

Sorting a list alphabetically is a bit more complicated when all the values are not in
lowercase. There are several ways to interpret capital letters when determining a sort
order, and specifying the exact order can be more complex than we want to deal with
at this time. However, most approaches to sorting will build directly on what you
learned in this section.

p. 45

Printing a List in Reverse Order

To reverse the original order of a list, you can use the reverse() method.
If we originally stored the list of cars in chronological order according to
when we owned them, we could easily rearrange the list into reverse chronological
order:
'''
games.reverse()
print(games)
'''
Notice that reverse() doesn’t sort backward alphabetically; it simply
reverses the order of the list:

['Zelda', 'NBA 2K', 'Mario', 'PGR']
['PGR', 'Mario', 'NBA 2K', 'Zelda']

The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time.
'''
games.reverse()
print(games)
'''

['Zelda', 'NBA 2K', 'Mario', 'PGR']

Finding the Length of a List

You can quickly find the length of a list by using the len() function. The list
in this example has four items, so its length is 4:

>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4

You’ll find len() useful when you need to identify the number of aliens
that still need to be shot down in a game, determine the amount of data
you have to manage in a visualization, or figure out the number of registered
users on a website, among other tasks.

Python counts the items in a list starting with one, so you shouldn’t run into any offby-
one errors when determining the length of a list.

p. 46-47 Avoiding Index Errors When Working with Lists

This example results in an index error:

Traceback (most recent call last):
File "motorcycles.py", line 2, in <module>
print(motorcycles[3])
IndexError: list index out of range

Python attempts to give you the item at index 3. But when it searches
the list, no item in motorcycles has an index of 3. Because of the off-by-one
nature of indexing in lists, this error is typical. People think the third item
is item number 3, because they start counting at 1. But in Python the third
item is number 2, because it starts indexing at 0.

An index error means Python can’t find an item at the index you
requested. If an index error occurs in your program, try adjusting the index
you’re asking for by one. Then run the program again to see if the results
are correct.

Keep in mind that whenever you want to access the last item in a list
you use the index -1. This will always work, even if your list has changed
size since the last time you accessed it:

Keep in mind that whenever you want to access the last item in a list
you use the index -1. This will always work, even if your list has changed
size since the last time you accessed it:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

The index -1 always returns the last item in a list, in this case the value
'suzuki':

The only time this approach will cause an error is when you request the
last item from an empty list:

motorcycles = []
print(motorcycles[-1])

No items are in motorcycles, so Python returns another index error:

Traceback (most recent call last):
File "motorcyles.py", line 3, in <module>
print(motorcycles[-1])
IndexError: list index out of range

'''
games = ['MGS']
print(games[-1])        # Works even with only one entry in the list.
nothing = []
# print(nothing[-1])      # doesn't work with an empty list, list index out of range
'''

Note - If an index error occurs and you can’t figure out how to resolve it, try printing your
list or just printing the length of your list. Your list might look much different than
you thought it did, especially if it has been managed dynamically by your program.
Seeing the actual list, or the exact number of items in your list, can help you sort out
such logical errors.

'''
