'''

p. 183 Chapter 10 - Files and Exceptions

You’ll learn about exceptions, which are special objects Python creates to
manage errors that arise while a program is running. You’ll also learn about
the json module, which allows you to save user data so it isn’t lost when your
program stops running.

p. 184-185 Reading from a File

p. Reading an Entire File

Here’s a program that opens this file, reads it, and prints the contents
of the file to the screen:

file_reader.py

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

To do any work with a file, even just printing its contents,
you first need to open the file to access it. The open() function needs
one argument: the name of the file you want to open. Python looks for this
file in the directory where the program that’s currently being executed is
stored.

The keyword with closes the file once access to it is no longer needed.
Notice how we call open() in this program but not close(). You could open
and close the file by calling open() and close(), but if a bug in your program
prevents the close() method from being executed, the file may never
close. This may seem trivial, but improperly closed files can cause data
to be lost or corrupted. And if you call close() too early in your program,
you’ll find yourself trying to work with a closed file (a file you can’t access),
which leads to more errors. It’s not always easy to know exactly when you
should close a file, but with the structure shown here, Python will figure that
out for you. All you have to do is open the file and work with it as desired,
trusting that Python will close it automatically when the with block finishes
execution.

Once we have a file object representing pi_digits.txt, we use the read()
method in the second line of our program to read the entire contents of
the file and store it as one long string in contents. When we print the value
of contents, we get the entire text file back:

3.1415926535
8979323846
2643383279

p. 185-186

File Paths

Because text_files is inside python_work, you could use a relative file path
to open a file from text_files. A relative file path tells Python to look for a
given location relative to the directory where the currently running program
file is stored. For example, you’d write:

with open('text_files/filename.txt') as file_object:

This line tells Python to look for the desired .txt file in the folder
text_files and assumes that text_files is located inside python_work (which
it is).

Note - Windows systems use a backslash (\\) instead of a forward slash (/) when
displaying file paths, but you can still use forward slashes in your code.

You can also tell Python exactly where the file is on your computer
regardless of where the program that’s being executed is stored. This
is called an absolute file path. You use an absolute path if a relative path
doesn’t work.

Absolute paths are usually longer than relative paths, so it’s helpful to
assign them to a variable and then pass that variable to open():
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:

Note - If you try to use backslashes in a file path, you’ll get an error because the backslash is used to escape characters in strings. For example, in the path "C:\\path\to\file.txt", the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape each one in the path, like this: "C:\\path\\to\\file.txt".

p. 187

Reading Line by Line

You can use a for loop on the file object to examine each line from a
file one at a time:

file_reader.py

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

At u we assign the name of the file we’re reading from to the variable
filename. This is a common convention when working with files. Because
the variable filename doesn’t represent the actual file—it’s just a string telling Python where to find the file—you can easily swap out 'pi_digits.txt'
for the name of another file you want to work with. After we call open(),
an object representing the file and its contents is assigned to the variable
file_object v. We again use the with syntax to let Python open and close
the file properly. To examine the file’s contents, we work through each line
in the file by looping over the file object w.

When we print each line, we find even more blank lines:

3.1415926535
8979323846
2643383279

These blank lines appear because an invisible newline character is at
the end of each line in the text file. The print function adds its own newline
each time we call it, so we end up with two newline characters at the
end of each line: one from the file and one from print(). Using rstrip()
on each line in the print() call eliminates these extra blank lines:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

Now the output matches the contents of the file once again:

3.1415926535
8979323846
2643383279

p, 188 Making a List of Lines from a File

The following example stores the lines of pi_digits.txt in a list inside the
with block and then prints the lines outside the with block:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

At u the readlines() method takes each line from the file and stores it
in a list. This list is then assigned to lines, which we can continue to work
with after the with block ends. At v we use a simple for loop to print each
line from lines. Because each item in lines corresponds to each line in the
file, the output matches the contents of the file exactly.

p. 188-189 Working with a File’s Contents

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

We start by opening the file and storing each line of digits in a list, just
as we did in the previous example. At u we create a variable, pi_string, to
hold the digits of pi. We then create a loop that adds each line of digits to
pi_string and removes the newline character from each line v. At w we
print this string and also show how long the string is:

3.1415926535 8979323846 2643383279
36

The variable pi_string contains the whitespace that was on the left
side of the digits in each line, but we can get rid of that by using strip()
instead of rstrip():
for line in lines:
    pi_string += line.strip()

Now we have a string containing pi to 30 decimal places. The string
is 32 characters long because it also includes the leading 3 and a decimal
point:

3.141592653589793238462643383279
32

Note - When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function.

p. 189-190 Large Files: One Million Digits

If we start with a text file that contains pi to 1,000,000 decimal places
instead of just 30, we can create a single string containing all these digits.
We don’t need to change our program at all except to pass it a different file.
We’ll also print just the first 50 decimal places, so we don’t have to watch a
million digits scroll by in the terminal:



filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

The output shows that we do indeed have a string containing pi to
1,000,000 decimal places:

3.14159265358979323846264338327950288419716939937510...
1000002

Python has no inherent limit to how much data you can work with; you
can work with as much data as your system’s memory can handle.

p. 190-191 is Your Birthday Contained in Pi?

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

At u we prompt for the user’s birthday, and then at v we check if that
string is in pi_string. Let’s try it:

Enter your birthdate, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!

p. 191 Writing to a File

p. 191-192 Writing to an Empty File

To write text to a file, you need to call open() with a second argument telling
Python that you want to write to the file. To see how this works, let’s write a
simple message and store it in a file instead of printing it to the screen:

write_message.py


filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
'
The call to open() in this example has two arguments u. The first argument
is still the name of the file we want to open. The second argument, 'w',
tells Python that we want to open the file in write mode. You can open a file
in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
you to read and write to the file ('r+'). If you omit the mode argument,
Python opens the file in read-only mode by default.

The open() function automatically creates the file you’re writing to if
it doesn’t already exist. However, be careful opening a file in write mode
('w') because if the file does exist, Python will erase the contents of the filebefore returning the file object.

At v we use the write() method on the file object to write a string to
the file. This program has no terminal output, but if you open the file
programming.txt, you’ll see one line:

Note - Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

p. 192 Writing Multiple Lines

The write() function doesn’t add any newlines to the text you write.
\
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

If you open programming.txt, you’ll see the two lines squished together:

I love programming.I love creating new games.

Including newlines in your calls to write() makes each string appear on
its own line:

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

The output now appears on separate lines:

I love programming.
I love creating new games.

You can also use spaces, tab characters, and blank lines to format your
output, just as you’ve been doing with terminal-based output.

p. 193 Appending to a File
If you want to add content to a file instead of writing over existing content,
you can open the file in append mode. When you open a file in append mode,
Python doesn’t erase the contents of the file before returning the file object.
Any lines you write to the file will be added at the end of the file. If the file doesn’t exist yet, Python will create an empty file for you.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love doing my thing in the terminal.\n")
    file_object.write("I love making these algorithms do what it do!\n")

At u we use the 'a' argument to open the file for appending rather
than writing over the existing file. At v we write two new lines, which are
added to programming.txt:

I love programming.
I love creating new games.
I love doing my thing in the terminal.
I love making these algorithms do what it do!

We end up with the original contents of the file, followed by the new
content we just added.

p. 194 Exceptions

Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python
unsure what to do next, it creates an exception object. If you write code
that handles the exception, the program will continue running. If you don’t
handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an exception
is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong. Instead of tracebacks, which can
be confusing for users to read, users will see friendly error messages that
you write.

p. 194 Handling the ZeroDivisionError Exception

print(5/0)

Of course Python can’t do this, so we get a traceback:

Traceback (most recent call last):
    File "division_calculator.py", line 1, in <module>
        print(5/0)
u ZeroDivisionError: division by zero

The error reported at u in the traceback, ZeroDivisionError, is an exception
object. Python creates this kind of object in response to a situation
where it can’t do what we ask it to. We can use this information to modify our program.

p. 194-195 Using try-except Blocks

Here’s what a try-except block for handling the ZeroDivisionError exception
looks like:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

We put print(5/0), the line that caused the error, inside a try block. If
the code in a try block works, Python skips over the except block. If the code
in the try block causes an error, Python looks for an except block whose
error matches the one that was raised and runs the code in that block.

In this example, the code in the try block produces a ZeroDivisionError,
so Python looks for an except block telling it how to respond. Python then
runs the code in that block, and the user sees a friendly error message
instead of a traceback:

You can't divide by zero!

If more code followed the try-except block, the program would continue
running because we told Python how to handle the error.

p. 195-196 Using Exceptions to Prevent Crashes

division_calculator.py

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:  ")
    if first_number == 'q':
        break
    second_number = input("Second number:  ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

This program prompts the user to input a first_number u and, if the
user does not enter q to quit, a second_number v. We then divide these two
numbers to get an answer w. This program does nothing to handle errors,
so asking it to divide by zero causes it to crash:

Give me two numbers, and I'll divide them.
Enter 'q' to quit.
First number: 5
Second number: 0
Traceback (most recent call last):
    File "division_calculator.py", line 9, in <module>
        answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero

p. 196-197 The else Block

We can make this program more error resistant by wrapping the line that
might produce errors in a try-except block. The error occurs on the line
that performs the division, so that’s where we’ll put the try-except block.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:  ")
    if first_number == 'q':
        break
    second_number = input("Second number:  ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    else:
        print(answer)

We ask Python to try to complete the division operation in a try
block u, which includes only the code that might cause an error. Any
code that depends on the try block succeeding is added to the else block.
In this case if the division operation is successful, we use the else block to
print the result w.

The except block tells Python how to respond when a ZeroDivisionError
arises v. If the try block doesn’t succeed because of a division by zero
error, we print a friendly message telling the user how to avoid this
kind of error. The program continues to run, and the user never sees
a traceback:

Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
You can't divide by 0!

The try-except-else block works like this: Python attempts to run the
code in the try block. The only code that should go in a try block is code
that might cause an exception to be raised. Sometimes you’ll have additional
code that should run only if the try block was successful; this code
goes in the else block. The except block tells Python what to do in case a
certain exception arises when it tries to run the code in the try block.

p. 197 Handling the FileNotFoundError Exception
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()

There are two changes here. One is the use of the variable f to represent
the file object, which is a common convention. The second is the use of
the encoding argument. This argument is needed when your system’s default
encoding doesn’t match the encoding of the file that’s being read.

Python can’t read from a missing file, so it raises an exception:

Traceback (most recent call last):
File "alice.py", line 3, in <module>
with open(filename, encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

In this example, the open() function produces the error, so to handle it, the
try block will begin with the line that contains open():


filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

In this example, the code in the try block produces a FileNotFoundError,
so Python looks for an except block that matches that error. Python then
runs the code in that block, and the result is a friendly error message
instead of a traceback:

Sorry, the file alice.txt does not exist.

p. 198-199 Analyzing Text

Let’s pull in the text of Alice in Wonderland and try to count the number
of words in the text. We’ll use the string method split(), which can build a
list of words from a string. Here’s what split() does with a string containing
just the title "Alice in Wonderland":

title = "Alice in Wonderland"

print(title.split())

['Alice', 'in', 'Wonderland']

The split() method separates a string into parts wherever it finds a
space and stores all the parts of the string in a list. The result is a list of
words from the string, although some punctuation may also appear with
some of the words. To count the number of words in Alice in Wonderland,
we’ll use split() on the entire text. Then we’ll count the items in the list to
get a rough idea of the number of words in the text:

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


I moved the file alice.txt to the correct directory, so the try block will
work this time. At u we take the string contents, which now contains the
entire text of Alice in Wonderland as one long string, and use the split()
method to produce a list of all the words in the book. When we use len() on
this list to examine its length, we get a good approximation of the number
of words in the original string v. At w we print a statement that reports
how many words were found in the file. This code is placed in the else block
because it will work only if the code in the try block was executed successfully. The output tells us how many words are in alice.txt:

The file alice.txt has about 12763 words.

p. 199-200 Working with Multiple Files

Let’s add more books to analyze. But before we do, let’s move the bulk of
this program to a function called count_words(). By doing so, it will be easier
to run the analysis for multiple books:



def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'alice.txt'
count_words(filename)

It’s a good habit to keep comments up to date
when you’re modifying a program, so we changed the comment to a docstring
and reworded it slightly u.

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)

The missing siddhartha.txt file has no effect on the rest of the program’s
execution:

The file alice.txt has about 29465 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.

Using the try-except block in this example provides two significant
advantages. We prevent our users from seeing a traceback, and we let the
program continue analyzing the texts it’s able to find. If we don’t catch
the FileNotFoundError that siddhartha.txt raised, the user would see a full
traceback, and the program would stop running after trying to analyze
Siddhartha. It would never analyze Moby Dick or Little Women.

p. 200 Falling Silently

To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block:



def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)


Now when a FileNotFoundError is raised, the code in
the except block runs, but nothing happens. No traceback is produced,
and there’s no output in response to the error that was raised. Users see
the word counts for each file that exists, but they don’t see any indication
that a file wasn’t found:

The file alice.txt has about 12763 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189092 words.

The pass statement also acts as a placeholder. It’s a reminder that you’re
choosing to do nothing at a specific point in your program’s execution
and that you might want to do something there later.

p. 201 Deciding Which Errors to Report

Giving users information they aren’t looking for can decrease the
usability of your program. Python’s error-handling structures give you finegrained control over how much to share with users when things go wrong;
it’s up to you to decide how much information to share.

p. 202-203 Storing Data

The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs. Even better,
the JSON data format is not specific to Python, so you can share data you
store in the JSON format with people who work in many other programming
languages. It’s a useful and portable format, and it’s easy to learn.

Note - The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python.

number_writer.py
'''
import json
'''
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


We first import the json module and then create a list of numbers to
work with. At u we choose a filename in which to store the list of numbers.
It’s customary to use the file extension .json to indicate that the data in
the file is stored in the JSON format. Then we open the file in write mode,
which allows json to write the data to the file v. At w we use the json.dump()
function to store the list numbers in the file numbers.json.

This program has no output, but let’s open the file numbers.json and
look at it. The data is stored in a format that looks just like Python:
[2, 3, 5, 7, 11, 13]

Now we’ll write a program that uses json.load() to read the list back into
memory:

number_reader.py


filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)


At u we make sure to read from the same file we wrote to. This time
when we open the file, we open it in read mode because Python only needs
to read from the file v. At w we use the json.load() function to load the
information stored in numbers.json, and we assign it to the variable numbers.
Finally we print the recovered list of numbers and see that it’s the same list
created in number_writer.py:

[2, 3, 5, 7, 11, 13]

This is a simple way to share data between two programs.

p. 204-205 Saving and Reading User-Generated Data


username = input('What is your name? ')

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f' We\'ll remember you when you come back, {username}!')


At u we prompt for a username to store. Next, we use json.dump(),
passing it a username and a file object, to store the username in a file v.
Then we print a message informing the user that we’ve stored their
information w:


filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f'Welcome back, {username}!')

At u we use json.load() to read the information stored in username.json
and assign it to the variable username. Now that we’ve recovered the username,
we can welcome them back v:

Welcome back, Eric!


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f'Welcome back, {username}!')


There’s no new code here; blocks of code from the last two examples
are just combined into one file. At u we try to open the file username.json.
If this file exists, we read the username back into memory v and print a
message welcoming back the user in the else block. If this is the first time
the user runs the program, username.json won’t exist and a FileNotFoundError
will occur w. Python will move on to the except block where we prompt the
user to enter their username x. We then use json.dump() to store the username
and print a greeting y.

Whichever block executes, the result is a username and an appropriate
greeting. If this is the first time the program runs, this is the output:

What is your name? Sam
We'll remember you when you come back, Sam!

Otherwise:

Welcome back, Sam!

This is the output you see if the program was already run at least once.

p. 206 Refactoring

Often, you’ll come to a point where your code will work, but you’ll recognize
that you could improve the code by breaking it up into a series of functions
that have specific jobs. This process is called refactoring. Refactoring
makes your code cleaner, easier to understand, and easier to extend.

The focus of remember_me.py is on greeting the user, so
let’s move all of our existing code into a function called greet_user():



def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('What is your name? ')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f'Welcome back, {username}!')


greet_user()

Let’s refactor greet_user() so it’s not doing so many different tasks.
We’ll start by moving the code for retrieving a stored username to a separate
function:



def getStoredUsername():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Greet the user by name."""
    username = getStoredUsername()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")


greet_user()

The new function get_stored_username() has a clear purpose, as stated
in the docstring at u. This function retrieves a stored username and returns
the username if it finds one. If the file username.json doesn’t exist, the function returns None v. This is good practice: a function should either return
the value you’re expecting, or it should return None. This allows us to perform
a simple test with the return value of the function. At w we print a
welcome back message to the user if the attempt to retrieve a username
was successful, and if it doesn’t, we prompt for a new username.

We should factor one more block of code out of greet_user(). If the
username doesn’t exist, we should move the code that prompts for a
new username to a function dedicated to that purpose:
'''


def getStoredUsername():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def getNewUserName():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = getStoredUsername()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = getNewUserName()
        print(f"We'll remember you when you come back, {username}!")


greet_user()

'''
Each function in this final version of remember_me.py has a single, clear
purpose. We call greet_user(), and that function prints an appropriate message:
it either welcomes back an existing user or greets a new user. It does
this by calling get_stored_username(), which is responsible only for retrieving
a stored username if one exists. Finally, greet_user() calls get_new_username()
if necessary, which is responsible only for getting a new username and storing
it. This compartmentalization of work is an essential part of writing
clear code that will be easy to maintain and extend.
'''
