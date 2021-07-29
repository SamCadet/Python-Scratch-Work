'''

p. 91 Chapter 6 - Dictionaries


p. 92 A Simple Dictionary
Consider a game featuring aliens that can have different colors and point
values. This simple dictionary stores information about a particular alien:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])

print(alien_0['points'])

The dictionary alien_0 stores the alien’s color and point value. The last
two lines access and display that information, as shown here:

green
5

As with most new programming concepts, using dictionaries takes
practice. Once you’ve worked with dictionaries for a bit you’ll soon see how
effectively they can model real-world situations.

p. 92-93

Working with Dictionaries

A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.

A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. Every key
is connected to its value by a colon, and individual key-value pairs are
separated by commas. You can store as many key-value pairs as you want in a
dictionary

p. 93 Accessing Values in a Dictionary

To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets, as shown here:

alien_0 = {'color': 'green'}
print(alien_0['color'])

This returns the value associated with the key 'color' from the dictionary

alien_0:
green

p. 93-94 Adding New Key-Value Pairs

to add a new key-value pair, you would give the name of the dictionary followed
by the new key in square brackets along with the new value.

alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

u alien_0['x_position'] = 0

v alien_0['y_position'] = 25

print(alien_0)

We start by defining the same dictionary that we’ve been working with.
We then print this dictionary, displaying a snapshot of its information. At u
we add a new key-value pair to the dictionary: key 'x_position' and value 0.
We do the same for key 'y_position' at v. When we print the modified dictionary,
we see the two additional key-value pairs:

{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}

The final version of the dictionary contains four key-value pairs. The
original two specify color and point value, and two more specify the alien’s
position.

Note - As of Python 3.7, dictionaries retain the order in which they were
defined. When you print a dictionary or loop through its elements, you will see
the elements in the same order in which they were added to the dictionary.

p. 94 Starting with an Empty Dictionary

To start filling an empty dictionary, define a dictionary with an empty set of
braces and then add each key-value pair on its own line.

alien_0 = {}    # or dict()

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


Here we define an empty alien_0 dictionary, and then add color and
point values to it. The result is the dictionary we’ve been using in previous
examples:

{'color': 'green', 'points': 5}

Typically, you’ll use empty dictionaries when storing user-supplied data
in a dictionary or when you write code that generates a large number of
key-value pairs automatically.

p. 95-96 Modifying Values in a Dictionary

To modify a value in a dictionary, give the name of the dictionary with the
key in square brackets and then the new value you want associated with
that key.

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

We first define a dictionary for alien_0 that contains only the alien’s
color; then we change the value associated with the key 'color' to 'yellow'.
The output shows that the alien has indeed changed from green to yellow:

The alien is green.
The alien is now yellow.

p. 96 Removing Key-Value Pairs

When you no longer need a piece of information that’s stored in a dictionary,
you can use the del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key that you want to
remove.


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

{'color': 'green', 'points': 5}
{'color': 'green'}

Note - Be aware that the deleted key-value pair is removed permanently.

p. 97 A Dictionary of Similar Objects

You can also use a dictionary to store one kind of information about many
objects.

their favorite programming language
is. A dictionary is useful for storing the results of a simple poll, like this:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

When you know you’ll need more than one line to define a dictionary, press enter
after the opening brace. Then indent the next line one level (four spaces),
and write the first key-value pair, followed by a comma. From this point
forward when you press enter, your text editor should automatically indent all
subsequent key-value pairs to match the first key-value pair.

Once you’ve finished defining the dictionary, add a closing brace on a
new line after the last key-value pair and indent it one level so it aligns with
the keys in the dictionary. It’s good practice to include a comma after the
last key-value pair as well, so you’re ready to add a new key-value pair on the
next line.

p. 98 Using get() to Access Values

Using keys in square brackets to retrieve the value you’re interested in
from a dictionary might cause one potential problem: if the key you ask for
doesn’t exist, you’ll get an error.

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

Traceback (most recent call last):
File "alien_no_points.py", line 2, in <module>
print(alien_0['points'])
KeyError: 'points'

For dictionaries, specifically, you can use the get() method to
set a default value that will be returned if the requested key doesn’t exist.
The get() method requires a key as a first argument. As a second
optional argument, you can pass the value to be returned if the key doesn’t
exist:

point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)

If the key 'points' exists in the dictionary, you’ll get the corresponding
value. If it doesn’t, you get the default value. In this case, points doesn’t
exist, and we get a clean message instead of an error:

No point value assigned.

If there’s a chance the key you’re asking for might not exist, consider
using the get() method instead of the square bracket notation.

Note If you leave out the second argument in the call to get() and the key
doesn’t exist, Python will return the value None. The special value None means
“no value exists.” This is not an error: it’s a special value meant to indicate
the absence of a value. You’ll see more uses for None in Chapter 8.

p. 99-100 Looping Through All Key-Value Pairs

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

You can access any single piece of information about user_0 based
on what you’ve already learned in this chapter. But what if you wanted to
see everything stored in this user’s dictionary? To do so, you could loop
through the dictionary using a for loop:

for key, value in user_0.items(): u
    print(f"\nKey: {key}") v
    print(f"Value: {value}") w


As shown at u, to write a for loop for a dictionary, you create names
for the two variables that will hold the key and value in each key-value
pair. You can choose any names you want for these two variables. This
code would work just as well if you had used abbreviations for the variable
names, like this:

for k, v in user_0.items()

The second half of the for statement at u includes the name of the
dictionary followed by the method items(), which returns a list of key-value
pairs. The for loop then assigns each of these pairs to the two variables provided.
In the preceding example, we use the variables to print each key v,
followed by the associated value w. The "\n" in the first print() call ensures
that a blank line is inserted before each key-value pair in the output:

Key: last
Value: fermi

Key: first
Value: enrico

Key: username
Value: efermi

Because the keys always
refer to a person’s name and the value is always a language, we’ll use the
variables name and language in the loop instead of key and value. This will
make it easier to follow what’s happening inside the loop:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items(): # u
    print(f"{name.title()}'s favorite language is {language.title()}.") # v

The code at u tells Python to loop through each key-value pair in the
dictionary. As it works through each pair the key is assigned to the variable
name, and the value is assigned to the variable language. These descriptive
names make it much easier to see what the print() call at v is doing.

Now, in just a few lines of code, we can display all of the information
from the poll:

Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.

p. 101-103 Looping Through All the Keys in a Dictionary

The keys() method is useful when you don’t need to work with all of the
values in a dictionary

for name in favorite_languages.keys(): # u
    print(name.title())

The line at u tells Python to pull all the keys from the dictionary
favorite_
languages and assign them one at a time to the variable name. The
output shows the names of everyone who took the poll:

Jen
Sarah
Edward
Phil

Looping through the keys is actually the default behavior when looping
through a dictionary, so this code would have exactly the same output if you
wrote . . .

for name in favorite_languages:

rather than . . .

for name in favorite_languages.keys():

You can choose to use the keys() method explicitly if it makes your code
easier to read, or you can omit it if you wish.

friends = ['phil', 'sarah'] # u

for name in favorite_languages.keys():
    print(name.title())

    if name in friends: # v
        language = favorite_languages[name].title() # w
        print(f"\t{name.title()}, I see you love {language}!")

At u we make a list of friends that we want to print a message to. Inside
the loop, we print each person’s name. Then at v we check whether the
name we’re working with is in the list friends. If it is, we determine the
person’s favorite language using the name of the dictionary and the current
value of name as the key w. We then print a special greeting, including a
reference to their language of choice.

Everyone’s name is printed, but our friends receive a special message:

Hi Jen.
Hi Sarah.
    Sarah, I see you love C!
Hi Edward.
Hi Phil.
    Phil, I see you love Python!

if 'erin' not in favorite_languages.keys(): # u
    print("Erin, please take our poll!")

The keys() method isn’t just for looping: it actually returns a list of all
the keys, and the line at u simply checks if 'erin' is in this list. Because
she’s not, a message is printed inviting her to take the poll:
Erin, please take our poll!

p. 103 Looping Through a Dictionary’s Keys in a Particular Order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

This for statement is like other for statements except that we’ve
wrapped the sorted() function around the dictionary.keys() method. This
tells Python to list all keys in the dictionary and sort that list before looping
through it. The output shows everyone who took the poll, with the names
displayed in order:

Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.

p. 104 Looping Through All Values in a Dictionary

If you are primarily interested in the values that a dictionary contains,
you can use the values() method to return a list of values without any keys.


print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

The for statement here pulls each value from the dictionary and assigns
it to the variable language. When these values are printed, we get a list of all
chosen languages:

The following languages have been mentioned:
Python
C
Python
Ruby

To see each language chosen without repetition, we can use a set.
A set is a collection in which each item must be unique:

for language in set(favorite_languages.values()): # u
    print(language.title())

When you wrap set() around a list that contains duplicate items, Python
identifies the unique items in the list and builds a set from those items. At u
we use set() to pull out the unique languages in favorite_
languages.values().

The result is a nonrepetitive list of languages that have been mentioned
by people taking the poll.

The following languages have been mentioned:
Python
C
Ruby

As you continue learning about Python, you’ll often find a built-in feature
of the language that helps you do exactly what you want with your data.

Note You can build a set directly using braces and separating the elements with
commas:

languages = {'python', 'ruby', 'python', 'c'}

print(languages)

{'ruby', 'python', 'c'}

It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
When you see braces but no key-value pairs, you’re probably looking at a set. Unlike
lists and dictionaries, sets do not retain items in any specific order.

games = {'super metroid', 'nba jam', 'mario', 'tetris', 'mario', }

print(games)

p. 106 Nesting

Sometimes you’ll want to store multiple dictionaries in a list, or a list of
items as a value in a dictionary. This is called nesting. You can nest dictionaries
inside a list, a list of items inside a dictionary, or even a dictionary inside
another dictionary. Nesting is a powerful feature, as the following examples
will demonstrate.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # u

for alien in aliens:
    print(alien)

We first create three dictionaries, each representing a different alien.
At u we store each of these dictionaries in a list called aliens. Finally, we
loop through the list and print out each alien:

{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

A more realistic example would involve more than three aliens with
code that automatically generates each alien. In the following example we
use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30): # u
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} # v
    aliens.append(new_alien) # w

# Show the first 5 aliens.
for alien in aliens[:5]: # x
    print(alien)
print("...")

# Show how many aliens have been created.

print(f"Total number of aliens: {len(aliens)}") # y

This example begins with an empty list to hold all of the aliens that
will be created. At u range() returns a series of numbers, which just tells
Python how many times we want the loop to repeat. Each time the loop
runs we create a new alien v and then append each new alien to the list
aliens w. At x we use a slice to print the first five aliens, and then at y we
print the length of the list to prove we’ve actually generated the full fleet of
30 aliens:

{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...

Total number of aliens: 30

These aliens all have the same characteristics, but Python considers
each one a separate object, which allows us to modify each alien
individually.

# Make 30 green aliens.
    --snip--

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

Because we want to modify the first three aliens, we loop through a
slice that includes only the first three aliens. All of the aliens are green now
but that won’t always be the case, so we write an if statement to make sure
we’re only modifying green aliens. If the alien is green, we change the color
to 'yellow', the speed to 'medium', and the point value to 10, as shown in the
following output:

{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}

You could expand this loop by adding an elif block that turns yellow
aliens into red, fast-moving ones worth 15 points each.

for alien in aliens[:3]:
    --snip--
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

It’s common to store a number of dictionaries in a list when each dictionary
contains many kinds of information about one object. For example,
you might create a dictionary for each user on a website, as we did in user.py
on page 100, and store the individual dictionaries in a list called users. All
of the dictionaries in the list should have an identical structure so you can
loop through the list and work with each dictionary object in the same way.

p. 108-109 A List in a Dictionary

# Store information about a pizza being ordered.
pizza = { u
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " v
    "with the following toppings:")

for topping in pizza['toppings']: w
    print("\t" + topping)

We begin at u with a dictionary that holds information about a
pizza that has been ordered. One key in the dictionary is 'crust', and
the associated value is the string 'thick'. The next key, 'toppings', has a
list as its value that stores all requested toppings. At v we summarize the
order before building the pizza. When you need to break up a long line
in a print() call, choose an appropriate point at which to break the line
being printed, and end the line with a quotation mark. Indent the next
line, add an opening quotation mark, and continue the string. Python
will automatically combine all of the strings it finds inside the parentheses.
To print the toppings, we write a for loop w. To access the list of
toppings, we use the key 'toppings', and Python grabs the list of toppings
from the dictionary.

The following output summarizes the pizza that we plan to build:
You ordered a thick-crust pizza with the following toppings:

mushrooms
extra cheese

favorite_languages = { u
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items(): v
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages: w
        print(f"\t{language.title()}")

As you can see at u the value associated with each name is now a
list. Notice that some people have one favorite language and others have
multiple favorites. When we loop through the dictionary at v, we use the
variable name languages to hold each value from the dictionary, because we
know that each value will be a list. Inside the main dictionary loop, we use
another for loop w to run through each person’s list of favorite languages.
Now each person can list as many favorite languages as they like:

Jen's favorite languages are:
    Python
    Ruby

Sarah's favorite languages are:
    C

Phil's favorite languages are:
    Python
    Haskell

Edward's favorite languages are:
    Ruby
    Go

Note - You should not nest lists and dictionaries too deeply. If you’re nesting
items much deeper than what you see in the preceding examples or you’re working
with someone else’s code with significant levels of nesting, most likely a
simpler way to solve the problem exists.

p. 110-111 A Dictionary in a Dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
},
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items(): u
    print(f"\nUsername: {username}") v
    full_name = f"{user_info['first']} {user_info['last']}" w
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}") x
    print(f"\tLocation: {location.title()}")

We first define a dictionary called users with two keys: one each for the
usernames 'aeinstein' and 'mcurie'. The value associated with each key is a
dictionary that includes each user’s first name, last name, and location. At u
we loop through the users dictionary. Python assigns each key to the variable
username, and the dictionary associated with each username is assigned to the
variable user_info. Once inside the main dictionary loop, we print the username
at v.

At w we start accessing the inner dictionary. The variable user_info,
which contains the dictionary of user information, has three keys: 'first',
'last', and 'location'. We use each key to generate a neatly formatted full
name and location for each person, and then print a summary of what we
know about each user x:

Notice that the structure of each user’s dictionary is identical. Although
not required by Python, this structure makes nested dictionaries easier to
work with. If each user’s dictionary had different keys, the code inside the
for loop would be more complicated.
'''
