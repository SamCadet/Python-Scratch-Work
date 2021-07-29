'''
Chapter 4

Working With Lists

In this chapter you’ll learn how to loop through an entire
list using just a few lines of code regardless of how long the list is. Looping
allows you to take the same action, or set of actions, with every item in a list.
As a result, you’ll be able to work efficiently with lists of any length, including
those with thousands or even millions of items.

p. 49-50 Looping Through an Entire List

When you want to do the same action with every item in a list, you can
use Python’s for loop.

Let’s say we have a list of magicians’ names, and we want to print out
each name in the list. We could do this by retrieving each name from the
list individually, but this approach could cause several problems. For one,
it would be repetitive to do this with a long list of names. Also, we’d have to
change our code each time the list’s length changed. A for loop avoids both
of these issues by letting Python manage these issues internally.
Let’s use a for loop to print out each name in a list of magicians:

magicians = ['alice', 'david', 'carolina']
for magician in magicians: v
    print(magician) w


At v, we define a for loop. This line tells Python to pull a name from the list
magicians, and associate it with the variable magician. At w we tell Python to
print the name that’s just been assigned to magician. Python then repeats
lines v and w, once for each name in the list. It might help to read this
code as “For every magician in the list of magicians, print the magician’s
name.” The output is a simple printout of each name in the list:

alice
david
carolina

p. 50-51

A Closer Look at Looping

The concept of looping is important because it’s one of the most common
ways a computer automates repetitive tasks. For example, in a simple loop
like we used in magicians.py, Python initially reads the first line of the loop:

for magician in magicians:

This line tells Python to retrieve the first value from the list magicians
and associate it with the variable magician. This first value is 'alice'. Python
then reads the next line:

print(magician)

Python prints the current value of magician, which is still 'alice'. Because
the list contains more values, Python returns to the first line of the loop:

for magician in magicians:

Python retrieves the next name in the list, 'david', and associates that
value with the variable magician. Python then executes the line:

print(magician)

Python prints the current value of magician again, which is now 'david'.
Python repeats the entire loop once more with the last value in the list,
'carolina'. Because no more values are in the list, Python moves on to the
next line in the program. In this case nothing comes after the for loop, so
the program simply ends.

When you’re using loops for the first time, keep in mind that the set of
steps is repeated once for each item in the list, no matter how many items
are in the list. If you have a million items in your list, Python repeats these
steps a million times—and usually very quickly.

Also keep in mind when writing your own for loops that you can choose
any name you want for the temporary variable that will be associated with
each value in the list. However, it’s helpful to choose a meaningful name
that represents a single item from the list. For example, here’s a good way to
start a for loop for a list of cats, a list of dogs, and a general list of items:

for cat in cats:
for dog in dogs:
for item in list_of_items:
These naming conventions

These naming conventions can help you follow the action being done
on each item within a for loop. Using singular and plural names can help
you identify whether a section of code is working with a single element from
the list or the entire list.

p. 51 Doing More Work Within a for Loop

You can do just about anything with each item in a for loop. Let’s build on
the previous example by printing a message to each magician, telling them
that they performed a great trick:

rappers = ['Master P', 'Silkk The Shocker', 'C-Murder']
for rapper in rappers:
    print(f'That man {rapper.title()} held it down for the whole Calliope!')

The only difference in this code is at u where we compose a message to
each magician, starting with that magician’s name. The first time through
the loop the value of magician is 'alice', so Python starts the first message
with the name 'Alice'. The second time through the message will begin with
'David', and the third time through the message will begin with 'Carolina'.
The output shows a personalized message for each magician in the list:

That man Master P held it down for the whole Calliope!
That man Silkk The Shocker held it down for the whole Calliope!
That man C-Murder held it down for the whole Calliope!

You can also write as many lines of code as you like in the for loop.
Every indented line following the line for magician in magicians is considered
inside the loop, and each indented line is executed once for each value in the list.
Therefore, you can do as much work as you like with each value in the list.

Let’s add a second line to our message, telling each magician that we’re
looking forward to their next trick:

for rapper in rappers:
    print(f'That man {rapper.title()} held it down for the whole Calliope!')
    print(f'Shout out to the No Limit Soulja, {rapper.title()}!\n')

Because we have indented both calls to print(), each line will be executed
once for every magician in the list. The newline ("\n") in the second print()
call u inserts a blank line after each pass through the loop. This creates a set
of messages that are neatly grouped for each person in the list:

That man Master P held it down for the whole Calliope!
Shout out to the No Limit Soulja, Master P!

That man Silkk The Shocker held it down for the whole Calliope!
Shout out to the No Limit Soulja, Silkk The Shocker!

That man C-Murder held it down for the whole Calliope!
Shout out to the No Limit Soulja, C-Murder!

You can use as many lines as you like in your for loops. In practice you’ll
often find it useful to do a number of different operations with each item in
a list when you use a for loop.

p. 52-53 Doing Something After a for Loop

Any lines of code after the for loop that are not indented are executed
once without repetition. Let’s write a thank you to the group of magicians
as a whole, thanking them for putting on an excellent show. To display this
group message after all of the individual messages have been printed, we
place the thank you message after the for loop without indentation:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
u print("Thank you, everyone. That was a great magic show!")

The first two calls to print() are repeated once for each magician in the
list, as you saw earlier. However, because the line at u is not indented, it’s
printed only once:

Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!

When you’re processing data using a for loop, you’ll find that this is a
good way to summarize an operation that was performed on an entire data
set. For example, you might use a for loop to initialize a game by running
through a list of characters and displaying each character on the screen.
You might then write some additional code after this loop that displays a
Play Now button after all the characters have been drawn to the screen.

p. 53 Avoiding Indentation Errors

Python’s use of indentation makes code very easy to read.
Basically, it uses whitespace to force you to write neatly formatted code
with a clear visual structure.

As you begin to write code that relies on proper indentation, you’ll
need to watch for a few common indentation errors. For example, people
sometimes indent lines of code that don’t need to be indented or forget
to indent lines that need to be indented. Seeing examples of these errors
now will help you avoid them in the future and correct them when they do
appear in your own programs.

p. 53-54 Forgetting to Indent
About indentation error, already know to indent

p. 54 Forgetting to Indent Additional Lines

this is what happens when we forget to indent the second
line in the loop that tells each magician we’re looking forward to their next
trick:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
u print(f"I can't wait to see your next trick, {magician.title()}.\n")

The call to print() u is supposed to be indented, but because Python
finds at least one indented line after the for statement, it doesn’t report an
error. As a result, the first print() call is executed once for each name in the
list because it is indented. The second print() call is not indented, so it is
executed only once after the loop has finished running. Because the final
value associated with magician is 'carolina', she is the only one who receives
the “looking forward to the next trick” message:

Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

This is a logical error. The syntax is valid Python code, but the code does
not produce the desired result because a problem occurs in its logic. If you
expect to see a certain action repeated once for each item in a list and it’s
executed only once, determine whether you need to simply indent a line or
a group of lines.

p. 55 Indenting Unnecessarily
Just about indenting when you don't need too outside of loops, already know this

p. 55-56 Indenting Unnecessarily After the Loop
Usually a logical error, already know it'll repeat however many times in the loop

p. 56 Forgetting the Colon
Colons are needed for Python to know you're using a loop, you'll get a syntax
error without them, already know this.

Although this is an easy error to fix, it’s not always an easy error to find. You’d be
surprised by the amount of time programmers spend hunting down singlecharacter
errors like this. Such errors are difficult to find because we often
just see what we expect to see.

p. 57 Making Numerical Lists

Many reasons exist to store a set of numbers. For example, you’ll need to
keep track of the positions of each character in a game, and you might want
to keep track of a player’s high scores as well. In data visualizations, you’ll
almost always work with sets of numbers, such as temperatures, distances,
population sizes, or latitude and longitude values, among other types of
numerical sets.

Lists are ideal for storing sets of numbers, and Python provides a
variety of tools to help you work efficiently with lists of numbers. Once you
understand how to use these tools effectively, your code will work well even
when your lists contain millions of items.

p. 56-57 Using the range() Function

Python’s range() function makes it easy to generate a series of numbers.
For example, you can use the range() function to print a series of numbers

like this:
for value in range(1, 5):
    print(value)

Although this code looks like it should print the numbers from 1 to 5, it
doesn’t print the number 5:

1
2
3
4

In this example, range() prints only the numbers 1 through 4. This is
another result of the off-by-one behavior you’ll see often in programming
languages. The range() function causes Python to start counting at the first
value you give it, and it stops when it reaches the second value you provide.
Because it stops at that second value, the output never contains the end
value, which would have been 5 in this case.
To print the numbers from 1 to 5, you would use range(1, 6):

for value in range(1, 6):
    print(value)
This time the output starts at 1 and ends at 5:

1
2
3
4
5

If your output is different than what you expect when you’re using
range(), try adjusting your end value by 1.

You can also pass range() only one argument, and it will start the
sequence of numbers at 0. For example, range(6) would return the numbers
from 0 through 5.

p. 58-59 Using range() to Make a List of Numbers

If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers.
In the example in the previous section, we simply printed out a series of
numbers. We can use list() to convert that same set of numbers into a list:

numbers = list(range(1, 6))
print(numbers)

And this is the result:
[1, 2, 3, 4, 5]

numbers = list(range(3, 9))
print(numbers)


We can also use the range() function to tell Python to skip numbers in a
given range. If you pass a third argument to range(), Python uses that value
as a step size when generating numbers.

For example, here’s how to list the even numbers between 1 and 10:

even_numbers.py

even_numbers = list(range(2, 11, 2))
print(even_numbers)

In this example, the range() function starts with the value 2 and then
adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
value, 11, and produces this result:

[2, 4, 6, 8, 10]

oddNumbers = list(range(1, 14, 2))
print(oddNumbers)

You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the first 10
square numbers (that is, the square of each integer from 1 through 10). In
Python, two asterisks (**) represent exponents. Here’s how you might put
the first 10 square numbers into a list:

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

We start with an empty list called squares u. At v, we tell Python to loop
through each value from 1 to 10 using the range() function. Inside the loop,
the current value is raised to the second power and assigned to the variable
square w. At x, each new value of square is appended to the list squares.
Finally, when the loop has finished running, the list of squares is printed y:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

To write this code more concisely, omit the temporary variable square
and append each new value directly to the list:


squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

The code at u does the same work as the lines at w and x in squares.py.
Each value in the loop is raised to the second power and then immediately
appended to the list of squares.

You can use either of these two approaches when you’re making more
complex lists. Sometimes using a temporary variable makes your code easier
to read; other times it makes the code unnecessarily long. Focus first on
writing code that you understand clearly, which does what you want it to do.
Then look for more efficient approaches as you review your code.

p. 59 Simple Statistics with a List of Numbers

A few Python functions are helpful when working with lists of numbers. For
example, you can easily find the minimum, maximum, and sum of a list of
numbers:

>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45

The examples in this section use short lists of numbers in order to fit easily on the
page. They would work just as well if your list contained a million or more numbers.


digits = [45, 34, 256, -21, 57]

print(sum(digits))

p. 59-60

List Comprehensions
The approach described earlier for generating the list squares consisted of
using three or four lines of code. A list comprehension allows you to generate
this same list in just one line of code. A list comprehension combines the
for loop and the creation of new elements into one line, and automatically
appends each new element. List comprehensions are not always presented
to beginners, but I have included them here because you’ll most likely see
them as soon as you start looking at other people’s code.

The following example builds the same list of square numbers you saw
earlier but uses a list comprehension:


squares = [value**2 for value in range(1, 11)]
print(squares)

To use this syntax, begin with a descriptive name for the list, such as
squares. Next, open a set of square brackets and define the expression for
the values you want to store in the new list. In this example the expression
is value**2, which raises the value to the second power. Then, write
a for loop to generate the numbers you want to feed into the expression,
and close the square brackets. The for loop in this example is for value
in range(1, 11), which feeds the values 1 through 10 into the expression
value**2. Notice that no colon is used at the end of the for statement.
The result is the same list of square numbers you saw earlier:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

When you’re writing three or four lines of code to generate lists and it
begins to feel repetitive, consider writing your own list comprehensions.

p. 61 Working with Part of a List

You can also work with a specific group of items in a list, which Python calls
a slice.

To make a slice, you specify the index of the first and last elements you
want to work with. As with the range() function, Python stops one item
before the second index you specify.

I know this already. First index is always included and the last isn't

So [1:4] would skip the item at index 0 grab the 1, 2, 3 indexes in the list
i.e. the second, third and fourth.

If you omit the first index in a slice, Python automatically starts your
slice at the beginning of the list:

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[:4])

Without a starting index, Python starts at the beginning of the list:

['charles', 'martina', 'michael', 'florence']

A similar syntax works if you want a slice that includes the end of a list.
For example, if you want all items from the third item through the last item,
you can start with index 2 and omit the second index:

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[2:])

Python returns all items from the third item through the end of the list:

['michael', 'florence', 'eli']

This syntax allows you to output all of the elements from any point in
your list to the end regardless of the length of the list. Recall that a negative
index returns an element a certain distance from the end of a list;
therefore, you can output any slice from the end of a list. For example, if
we want to output the last three players on the roster, we can use the slice
players[-3:]:

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

This prints the names of the last three players and would continue to
work as the list of players changes in size.
'''
people = ['jamal', 'darryl', 'betty', 'keisha', 'tasha']
print(people[-3:])
print(people[:-3])
'''
['betty', 'keisha', 'tasha'] [-3:] starts from the back and includes the last three names
['jamal', 'darryl'] starts from the front and includes only the first two names

blank spaces before and after each example are interpreted by Python as 0

You can include a third value in the brackets indicating a slice. If a third value is
included, this tells Python how many items to skip between items in the specified
range.

You can use a slice in a for loop if you want to loop through a subset of
the elements in a list. In the next example we loop through the first three
players and print their names as part of a simple roster:

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]: u
    print(player.title())

Instead of looping through the entire list of players at u, Python loops
through only the first three names:

Here are the first three players on my team:
Charles
Martina
Michael

Slices are very useful in a number of situations. For instance, when you’re
creating a game, you could add a player’s final score to a list every time that
player finishes playing. You could then get a player’s top three scores by sorting
the list in decreasing order and taking a slice that includes just the first
three scores. When you’re working with data, you can use slices to process
your data in chunks of a specific size. Or, when you’re building a web application,
you could use slices to display information in a series of pages with
an appropriate amount of information on each page.

p. 63 Copying a List

To copy a list, you can make a slice that includes the entire original list
by omitting the first index and the second index ([:]). This tells Python to
make a slice that starts at the first item and ends with the last item, producing
a copy of the entire list.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] v

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

At u we make a list of the foods we like called my_foods. At v we make a
new list called friend_foods. We make a copy of my_foods by asking for a slice
of my_foods without specifying any indices and store the copy in friend_foods.
When we print each list, we see that they both contain the same foods:

My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']

To prove that we actually have two separate lists, we’ll add a new food
to each list and show that each list keeps track of the appropriate person’s
favorite foods:

my_foods = ['pizza', 'falafel', 'carrot cake']
u friend_foods = my_foods[:]

v my_foods.append('cannoli')
w friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

At u we copy the original items in my_foods to the new list friend_foods, as
we did in the previous example. Next, we add a new food to each list: at v we
add 'cannoli' to my_foods, and at w we add 'ice cream' to friend_foods. We then
print the two lists to see whether each of these foods is in the appropriate list.

My favorite foods are:
x ['pizza', 'falafel', 'carrot cake', 'cannoli']
My friend's favorite foods are:
y ['pizza', 'falafel', 'carrot cake', 'ice cream']

The output at x shows that 'cannoli' now appears in our list of favorite
foods but 'ice cream' doesn’t. At y we can see that 'ice cream' now appears
in our friend’s list but 'cannoli' doesn’t. If we had simply set friend_foods
equal to my_foods, we would not produce two separate lists. For example,
here’s what happens when you try to copy a list without using a slice:

Instead of storing a copy of my_foods in friend_foods at u, we set friend
_foods equal to my_foods. This syntax actually tells Python to associate
the new variable friend_foods with the list that is already associated with
my_foods, so now both variables point to the same list. As a result, when we
add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice
cream' will appear in both lists, even though it appears to be added only to
friend_foods.

The output shows that both lists are the same now, which is not what we
wanted:

My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

p. 65 Tuples

sometimes you’ll want to create a list of items that cannot
change. Tuples allow you to do just that. Python refers to values that cannot
change as immutable, and an immutable list is called a tuple.

p. 66 Defining a Tuple
A tuple looks just like a list except you use parentheses instead of square
brackets. Once you define a tuple, you can access individual elements by
using each item’s index, just as you would for a list.

Let’s see what happens if we try to change one of the items in the tuple
dimensions:

dimensions = (200, 50)
u dimensions[0] = 250

The code at u tries to change the value of the first dimension, but
Python returns a type error. Basically, because we’re trying to alter a tuple,
which can’t be done to that type of object, Python tells us we can’t assign a
new value to an item in a tuple:

Traceback (most recent call last):
File "dimensions.py", line 2, in <module>
dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment

This is beneficial because we want Python to raise an error when a line
of code tries to change the dimensions of the rectangle.

Tuples are technically defined by the presence of a comma; the parentheses make them
look neater and more readable. If you want to define a tuple with one element, you
need to include a trailing comma:

my_t = (3,)

It doesn’t often make sense to build a tuple with one element, but this can happen
when tuples are generated automatically.

p. 67 Looping Through All Values in a Tupl
e
You can loop over all the values in a tuple using a for loop, just as you did
with a list:

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

Python returns all the elements in the tuple, just as it would for a list:

200
50

Writing over a Tuple

Although you can’t modify a tuple, you can assign a new value to a variable
that represents a tuple. So if we wanted to change our dimensions, we could
redefine the entire tuple:
u dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

v dimensions = (400, 100)
w print("\nModified dimensions:")

for dimension in dimensions:
    print(dimension)

The lines starting at u define the original tuple and print the initial
dimensions. At v, we associate a new tuple with the variable dimensions. We
then print the new dimensions at w. Python doesn’t raise any errors this
time, because reassigning a variable is valid:

Original dimensions:
200
50

Modified dimensions:
400
100

When compared with lists, tuples are simple data structures. Use them
when you want to store a set of values that should not be changed throughout
the life of a program.

p. 68 Styling Your Code
basically about PEP8, shout out to anaconda yooo

p. 69 Indentation

You should definitely use your tab key,
but also make sure your editor is set to insert spaces rather than tabs into
your document.

Mixing tabs and spaces in your file can cause problems that are very
difficult to diagnose. If you think you have a mix of tabs and spaces, you
can convert all tabs in a file to spaces in most editors.

Line Length
Many Python programmers recommend that each line should be less than
80 characters.

PEP 8 also recommends that you limit
all of your comments to 72 characters per line, because some of the tools
that generate automatic documentation for larger projects add formatting
characters at the beginning of each commented line.

Appendix B shows you how to configure your text editor so it always inserts four
spaces each time you press the tab key and shows a vertical guideline to help you
follow the 79-character limit.

p. 69-70 Blank Lines
To group parts of your program visually, use blank lines. You should use
blank lines to organize your files, but don’t do so excessively.

Blank lines won’t affect how your code runs, but they will affect the
readability of your code. The Python interpreter uses horizontal indentation
to interpret the meaning of your code, but it disregards vertical
spacing.
'''
