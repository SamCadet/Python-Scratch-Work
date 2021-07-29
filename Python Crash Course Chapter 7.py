'''
p. 113 Chapter 7 User Input and While Loops

p. 114 How the input() Function Works

The input() function pauses your program and waits for the user to enter
some text. Once Python receives the user’s input, it assigns that input to a
variable to make it convenient for you to work with.

The input() function takes one argument: the prompt, or instructions,
that we want to display to the user so they know what to do.

The program waits while the user enters
their response and continues after the user presses enter.

p. 114-115

Writing Clear Prompts

Each time you use the input() function, you should include a clear, easy-to
follow prompt that tells the user exactly what kind of information you’re
looking for.

Add a space at the end of your prompts (after the colon in the preceding
example) to separate the prompt from the user’s response and to make
it clear to your user where to enter their text.

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

Please enter your name: Eric
Hello, Eric!


Sometimes you’ll want to write a prompt that’s longer than one line.
For example, you might want to tell the user why you’re asking for certain
input. You can assign your prompt to a variable and pass that variable to the
input() function. This allows you to build your prompt over several lines,
then write a clean input() statement.

greeter.py

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

This example shows one way to build a multi-line string. The first line
assigns the first part of the message to the variable prompt. In the second
line, the operator += takes the string that was assigned to prompt and adds
the new string onto the end.

The prompt now spans two lines, again with space after the question
mark for clarity:

If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric
Hello, Eric!

p. 115 Using int() to Accept Numerical Input

When you use the input() function, Python interprets everything the user
enters as a string.

The int() function converts a string representation of a number to a numerical
representation, as shown here:

>>> age = input("How old are you? ")
How old are you? 21
u >>> age = int(age)
>>> age >= 18
True

When you use numerical input to do calculations and comparisons,
be sure to convert the input value to a numerical representation first.

p. 116 The Modulo Operator
A useful tool for working with numerical information is the modulo operator (%),
which divides one number by another number and returns the remainder:

>>> 4 % 3
1

The modulo operator doesn’t tell you how many times one number fits
into another; it just tells you what the remainder is.

When one number is divisible by another number, the remainder is 0,
so the modulo operator always returns 0. You can use this fact to determine
if a number is even or odd:

even_or_odd.py

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

Even numbers are always divisible by two, so if the modulo of a number
and two is zero (here, if number % 2 == 0) the number is even. Otherwise,
it’s odd.

Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.

p. 118 Introducing while Loops

The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true.

p. 118-119 Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"

prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

message is blank until the user types in anything, the program will just
repeat the user's message as long as the user's input doesn't equal quit.





prompt = "\nTell me something, and I will repeat it back to you:"

prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


from parrot program on p. 119

If you add the if statement as seen above then the program won't print quit
anymore as a message. It'll just close.

p. 120 Using a Flag

For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program
is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop
running when any of several events sets the value of the flag to False.
As a result, our overall while statement needs to check only one condition:
whether or not the flag is currently True. Then, all our other tests (to see if
an event has occurred that should set the flag to False) can be neatly
organized in the rest of the program.


prompt = "\nTell me something, and I will repeat it back to you:"

prompt += "\nEnter 'quit' to end the program. "

message = ""

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

Making the variable active = True starts the program and keeps it running until
the user types quit. That way you don't have to make any comparison and use
the variable in other parts of the program at the same time. active turns to
false if the user inputs quit and closes the program.

You gain more flexibility to add if and elif statements for many
events that'd cause the program to close.

p. 121 Using break to Exit a Loop

To exit a while loop immediately without running any remaining code in the
loop, regardless of the results of any conditional test, use the break
statement.

Note - You can use the break statement in any of Python’s loops. For example,
you could use break to quit a for loop that’s working through a list or a
dictionary.

p. 122 Using continue in a Loop

Rather than breaking out of a loop entirely without executing the rest of its
code, you can use the continue statement to return to the beginning of the
loop based on the result of a conditional test.
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


This starts with the current_number at 0. Then, the while loop says as long as
the current_number is less than 10, add 1. Then from one, if the current number
is divisible by two, ignore the rest of the loop and
return to the beginning. Then it goes through the rest of the loop and only adds
numbers that aren't divisble by two.

so 1, skips 2 since it's divisible by zero, 3, skips 4 and so on.

p. 122-123 Avoiding Infinite Loops

Every while loop needs a way to stop running so it won’t continue to run forever.
For example, this counting loop should count from 1 to 5:
counting.py

x = 1
while x <= 5:
    print(x)
    x += 1

But if you accidentally omit the line x += 1 (as shown next), the loop
will run forever:
'
# This loop runs forever!
x = 1
while x <= 5:
    print(x)

Now the value of x will start at 1 but never change. As a result, the
conditional test x <= 5 will always evaluate to True and the while loop will
run forever, printing a series of 1s, like this:

1
1
1
1
--snip--

To avoid writing infinite loops, test every while loop and make sure
the loop stops when you expect it to. If you want your program to end
when the user enters a certain input value, run the program and enter
that value. If the program doesn’t end, scrutinize the way your program
handles the value that should cause the loop to exit. Make sure at least
one part of the program can make the loop’s condition False or cause it
to reach a break statement.

Note - Sublime Text and some other editors have an embedded output window. This
can make it difficult to stop an infinite loop, and you might have to close the
editor to end the loop. Try clicking in the output area of the editor before
pressing ctrl-C, and you should be able to cancel an infinite loop.

p. 124 Using a while Loop with Lists and Dictionaries

A for loop is effective for looping through a list, but you shouldn’t modify
a list inside a for loop because Python will have trouble keeping track of the
items in the list. To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store, and
organize lots of input to examine and report on later.

confirmed _users.py
'''
# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
the while uncomformed_users loop remains true as long as the list
has values in it

.pop() takes the last entry and adds it to the current user variable.
then a message appears saying the user's getting verified before it gets
added to the empty confirmed users list.

After that, the program prints a message to show which users have been added to
the confirmed users list. Then the program ends.

Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
[Finished in 0.1s]

p. 125-126 Removing All Instances of Specific Values from a List

pets.py

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

First the pets list gets printed with all the copies of 'cat' in it.

The while loop uses the remove() method to erase all the mentions of cat in the
list. The loop stays true until the list doesn't have 'cat' in it anymore.

Finally, the program prints the 'cat'-free list.

p. 126 Filling a Dictionary with User Input

mountain_poll.py
'''
responses = {}

# Set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
'''
responses gets set to an empty dictionary. then it makes polling_active a flag
as True for the while loop

the while loop starts with polling_active, asks for name and response from
the user input

then the users name and response get stored in the response dictionary as
key/value pairs

then the loop asks if they want to let someone else answer the poll, if no then
polling_active becomes false and the loop breaks

the program prints the poll results line and starts a for loop with
responses.items() to access the key/value pairs in responses. Finally it
prints the key/value pairs within the f string.
'''

