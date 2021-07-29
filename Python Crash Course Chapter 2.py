'''
p. 17 Naming and Using Variables

When you’re using variables in Python, you need to adhere to a few rules
and guidelines. Breaking some of these rules will cause errors; other guidelines
just help you write code that’s easier to read and understand. Be sure
to keep the following variable rules in mind:

• Variable names can contain only letters, numbers, and underscores.
They can start with a letter or an underscore, but not with a number.
For instance, you can call a variable message_1 but not 1_message.

• Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names. For example, greeting_message
works, but greeting message will cause errors.

• Avoid using Python keywords and function names as variable names;
that is, do not use words that Python has reserved for a particular programmatic
purpose, such as the word print. (See “Python Keywords
and Built-in Functions” on page 471.)

• Variable names should be short but descriptive. For example, name is
better than n, student_name is better than s_n, and name_length is better
than length_of_persons_name.

• Be careful when using the lowercase letter l and the uppercase letter O
because they could be confused with the numbers 1 and 0.

p. 18-19 Variables Are Labels

Variables are often described as boxes you can store values in. This idea can
be helpful the first few times you use a variable, but it isn’t an accurate way
to describe how variables are represented internally in Python. It’s much
better to think of variables as labels that you can assign to values. You can
also say that a variable references a certain value.

This distinction probably won’t matter much in your initial programs,
but it’s worth learning earlier rather than later. At some point, you’ll see
unexpected behavior from a variable, and an accurate understanding of
how variables work will help you identify what’s happening in your code.

2-1. Simple Message: Assign a message to a variable, and then print that
message.
2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change

'''
message = 'yo'
print(message)
message = 'myguy'
print(message)
'''
p. 19 Strings
A string is a series of characters. Anything inside quotes is considered
a string in Python, and you can use single or double quotes around your
strings like this:

"This is a string."
'This is also a string.'

p. 20 Changing Case in a String with Methods

One of the simplest tasks you can do with strings is change the case of the
words in a string. Look at the following code, and try to determine what’s
happening:

name = "ada lovelace"

print(name.title())

Save this file as name.py, and then run it. You should see this output:

Ada Lovelace

In this example, the variable name refers to the lowercase string "ada
lovelace". The method title() appears after the variable in the print() call.
A method is an action that Python can perform on a piece of data. The dot
(.) after name in name.title() tells Python to make the title() method act on
the variable name. Every method is followed by a set of parentheses, because
methods often need additional information to do their work. That information
is provided inside the parentheses. The title() function doesn’t need
any additional information, so its parentheses are empty.

The title() method changes each word to title case, where each word
begins with a capital letter. This is useful because you’ll often want to think
of a name as a piece of information. For example, you might want your program
to recognize the input values Ada, ADA, and ada as the same name, and
display all of them as Ada.

Several other useful methods are available for dealing with case as
well. For example, you can change a string to all uppercase or all lowercase
letters
like this:

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

This will display the following:
ADA LOVELACE
ada lovelace

The lower() method is particularly useful for storing data. Many times
you won’t want to trust the capitalization that your users provide, so you’ll
convert strings to lowercase before storing them. Then when you want to
display the information, you’ll use the case that makes the most sense for
each string.
name.py

p. 21

Using Variables in Strings
In some situations, you’ll want to use a variable’s value inside a string. For
example, you might want two variables to represent a first name and a last
name respectively, and then want to combine those values to display someone’s
full name:
'''
firstName = 'ada'
lastName = 'wong'
fullName = f'{firstName} {lastName}'
print(fullName)
'''
To insert a variable’s value into a string, place the letter f immediately
before the opening quotation mark . Put braces around the name or names
of any variable you want to use inside the string. Python will replace each
variable with its value when the string is displayed.

These strings are called f-strings. The f is for format, because Python
formats the string by replacing the name of any variable in braces with its
value. The output from the previous code is:

ada wong

You can do a lot with f-strings. For example, you can use f-strings to
compose complete messages using the information associated with a variable,
as shown here:
'''
print(f"Hello, {fullName.title()}!")
'''
The full name is used in a sentence that greets the user , and the
title() method changes the name to title case. This code returns a simple
but nicely formatted greeting:

Hello, Ada Wong!

You can also use f-strings to compose a message, and then assign the
entire message to a variable:
'''
message = f"Hello, {fullName.title()}!"
print(message)
'''
This code displays the message Hello, Ada Lovelace! as well, but by
assigning the message to a variable  we make the final print() call much
simpler .

F-strings were first introduced in Python 3.6. If you’re using Python 3.5 or earlier,
you’ll need to use the format() method rather than this f syntax. To use format(), list
the variables you want to use in the string inside the parentheses following format.
Each variable is referred to by a set of braces; the braces will be filled by the values
listed in parentheses in the order provided:
full_name = "{} {}".format(first_name, last_name)

p. 22 Adding Whitespace to Strings with Tabs or Newlines

In programming, whitespace refers to any nonprinting character, such as
spaces, tabs, and end-of-line symbols. You can use whitespace to organize
your output so it’s easier for users to read.
To add a tab to your text, use the character combination \t as shown
at :
'''
print('\tWhoadie')
'''
To add a newline in a string, use the character combination \n:

You can also combine tabs and newlines in a single string. The string
"\n\t" tells Python to move to a new line, and start the next line with a tab.
The following example shows how you can use a one-line
string to generate four lines of output:
'''
print('Outkast:\n\tMe\n\tand you\n\tyo mama\n\tand yo cousin too')
'''
Outkast:
    Me
    and you
    yo mama
    and yo cousin too

Newlines and tabs will be very useful in the next two chapters when you
start to produce many lines of output from just a few lines of code

p. 22-23 Stripping Whitespace

Extra whitespace can be confusing in your programs. To programmers
'python' and 'python ' look pretty much the same. But to a program, they
are two different strings. Python detects the extra space in 'python ' and
considers it significant unless you tell it otherwise.

It’s important to think about whitespace, because often you’ll want to
compare two strings to determine whether they are the same. For example,
one important instance might involve checking people’s usernames when
they log in to a website. Extra whitespace can be confusing in much simpler
situations as well. Fortunately, Python makes it easy to eliminate extraneous
whitespace from data that people enter.

Python can look for extra whitespace on the right and left sides of a
string. To ensure that no whitespace exists at the right end of a string, use
the rstrip() method.
'''
name = 'Jason '
print(name)
print(name.rstrip())
print(name)
'''
Jason
Jason
Jason

The value associated with favorite_language at  contains extra whitespace
at the end of the string. When you ask Python for this value in a terminal
session, you can see the space at the end of the value . When the
rstrip() method acts on the variable favorite_language at , this extra space
is removed. However, it is only removed temporarily. If you ask for the value
of favorite_language again, you can see that the string looks the same as
when it was entered, including the extra whitespace .

To remove the whitespace from the string permanently, you have to
associate the stripped value with the variable name:
'''
name = 'Jason '
name = name.rstrip()
print(name)
'''
Jason

the right side of the string and then associate this new value with the
original variable, as shown at . Changing a variable’s value is done often
in programming. This is how a variable’s value can be updated as a program
is executed or in response to user input.
You can also strip whitespace from the left side of a string using the
lstrip() method, or from both sides at once using strip():
'''
name = ' John '
print(name.rstrip())
print(name.lstrip())
print(name.strip())
'''
 John
John
John

In this example, we start with a value that has whitespace at the beginning
and the end . We then remove the extra space from the right side
at , from the left side at , and from both sides at . Experimenting with
these stripping functions can help you become familiar with manipulating
strings. In the real world, these stripping functions are used most often to
clean up user input before it’s stored in a program.
'''
print('Joe\'s dog is named Whoadie.')
'''
p. 24 Avoiding Syntax Errors with Strings (already know this yoooo)

One kind of error that you might see with some regularity is a syntax error.
A syntax error occurs when Python doesn’t recognize a section of your program
as valid Python code. For example, if you use an apostrophe within
single quotes, you’ll produce an error. This happens because Python interprets
everything between the first single quote and the apostrophe as a
string. It then tries to interpret the rest of the text as Python code, which
causes errors.

Your editor’s syntax highlighting feature should help you spot some syntax errors
quickly as you write your programs. If you see Python code highlighted as if it’s
English or English highlighted as if it’s Python code, you probably have a mismatched
quotation mark somewhere in your file.

Syntax errors are also the least specific kind of error, so they
can be difficult and frustrating to identify and correct. If you get stuck on
a particularly stubborn error, see the suggestions in Appendix C.
p. 25-2 Numbers

Already know about Integers, operations and floats but I have to use print() to do operations
in Sublime Text.

p. 26 Floats

Python calls any number with a decimal point a float. This term is used
in most programming languages, and it refers to the fact that a decimal
point can appear at any position in a number. Every programming language
must be carefully designed to properly manage decimal numbers
so numbers behave appropriately no matter where the decimal point
appears.

But be aware that you can sometimes get an arbitrary number of decimal
places in your answer:

>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004

This happens in all languages and is of little concern. Python tries to
find a way to represent the result as precisely as possible, which is sometimes
difficult given how computers have to represent numbers internally. Just
ignore the extra decimal places for now; you’ll learn ways to deal with the
extra places when you need to in the projects in Part II.

p. 27 Integers and Floats

When you divide any two numbers, even if they are integers that result in a
whole number, you’ll always get a float:

>>> 4/2
2.0

If you mix an integer and a float in any other operation, you’ll get a
float as well:

>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0

Python defaults to a float in any operation that uses a float, even if the
output is a whole number.

Underscores in Numbers

When you’re writing long numbers, you can group digits using underscores
to make large numbers more readable:

>>> universe_age = 14_000_000_000

When you print a number that was defined using underscores, Python
prints only the digits:

>>> print(universe_age)
14000000000
'''
years = 10_000
print(years)
'''
Python ignores the underscores when storing these kinds of values.
Even if you don’t group the digits in threes, the value will still be unaffected.
To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature
works for integers and floats, but it’s only available in Python 3.6
and later.

p. 28 Multiple Assignment

You can assign values to more than one variable using just a single line.
This can help shorten your programs and make them easier to read; you’ll
use this technique most often when initializing a set of numbers.
For example, here’s how you can initialize the variables x, y, and z
to zero:
'''
x, y, z = 0, 0, 0

print(x, y, z)
'''
You need to separate the variable names with commas, and do the
same with the values, and Python will assign each value to its respectively
positioned variable. As long as the number of values matches the number of
variables, Python will match them up correctly.

Constants

A constant is like a variable whose value stays the same throughout the life
of a program. Python doesn’t have built-in constant types, but Python programmers
use all capital letters to indicate a variable should be treated as a
constant and never be changed:
'''
TIMESISHOULDALEFTYOASS = 1000
'''
When you want to treat a variable as a constant in your code, make the
name of the variable all capital letters.

2-8. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should simply be four lines with the number 8 appearing once
on each line.
'''
print(4 + 4)
print(10 - 2)
print(2 * 4)
# How'd ya do that? Exercise 2.10
print(int(8 / 1))
'''
2-9. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message.
'''
favNumber = 14
# This thang was easy. Exercise 2.10
print(f'My favorite number is {favNumber}.')
'''
p. 29-30 Comments, already know this...

Skilled programmers expect to see comments in code, so it’s best to start
adding descriptive comments to your programs now. Writing clear, concise
comments in your code is one of the most beneficial habits you can form as
a new programmer.

When you’re determining whether to write a comment, ask yourself if
you had to consider several approaches before coming up with a reasonable
way to make something work; if so, write a comment about your solution.
It’s much easier to delete extra comments later on than it is to go back
and write comments for a sparsely commented program. From now on, I’ll
use comments in examples throughout this book to help explain sections
of code.

2-10. Adding Comments: Choose two of the programs you’ve written, and
add at least one comment to each. If you don’t have anything specific to write
because your programs are too simple at this point, just add your name and
the current date at the top of each program file. Then write one sentence
describing what the program does.

p. 30 The Zen of Python

Just use import this and read it. It's a guideline to write clea code
for Python neckbeards.

Simple is better than complex.

If you have a choice between a simple and a complex solution, and both
work, use the simple solution. Your code will be easier to maintain, and it
will be easier for you and others to build on that code later on.

Complex is better than complicated.

Real life is messy, and sometimes a simple solution to a problem is
unattainable.

In that case, use the simplest solution that works.
Readability counts.

Even when your code is complex, aim to make it readable. When you’re
working on a project that involves complex coding, focus on writing informative
comments for that code.

There should be one-- and preferably only one --obvious way to do it.

If two Python programmers are asked to solve the same problem, they
should come up with fairly compatible solutions. This is not to say there’s
no room for creativity in programming. On the contrary! But much of programming
consists of using small, common approaches to simple situations
within a larger, more creative project. The nuts and bolts of your programs
should make sense to other Python programmers.

Now is better than never.

You could spend the rest of your life learning all the intricacies of Python
and of programming in general, but then you’d never complete any projects.
Don’t try to write perfect code; write code that works, and then decide
whether to improve your code for that project or move on to something new.

As you continue to the next chapter and start digging into more
involved topics, try to keep this philosophy of simplicity and clarity in mind.
Experienced programmers will respect your code more and will be happy
to give you feedback and collaborate with you on interesting projects.

2-11. Zen of Python: Enter import this into a Python terminal session and skim
through the additional principles.
'''
import this
