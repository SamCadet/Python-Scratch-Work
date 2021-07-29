'''
Chapter 5

If statements

let's try to condense the notes instead of copying everything yooooo

Python’s if statement allows you to examine the
current state of a program and respond appropriately
to that state.

p. 72 A Simple Example

The following code loops through a list of car
names and looks for the value 'bmw'. Whenever the value is 'bmw', it’s printed
in uppercase instead of title case:

cars.py

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
u   if car == 'bmw':
    print(car.upper())

else:
    print(car.title())

The loop in this example first checks if the current value of car is 'bmw' u.
If it is, the value is printed in uppercase. If the value of car is anything
other than 'bmw', it’s printed in title case:

Audi
BMW
Subaru
Toyota

p. 72 Conditional Tests

At the heart of every if statement is an expression that can be evaluated as
True or False and is called a conditional test. Python uses the values True and
False to decide whether the code in an if statement should be executed. If a
conditional test evaluates to True, Python executes the code following the if
statement. If the test evaluates to False, Python ignores the code following
the if statement.

p. 72-73 Checking for Equality

(==) This equality operator returns True if the values on the left and right
side of the operator match, and False if they don’t match.

A single equal sign is really a statement; you might read the code at u
as “Set the value of car equal to 'audi'.” On the other hand, a double equal
sign, like the one at v, asks a question: “Is the value of car equal to 'bmw'?”
Most programming languages use equal signs in this way.

p. 73 Ignoring Case When Checking for Equality

>>> car = 'Audi'
>>> car.lower() == 'audi'
True

This test would return True no matter how the value 'Audi' is formatted
because the test is now case insensitive. The lower() function doesn’t change
the value that was originally stored in car, so you can do this kind of
comparison without affecting the original variable:

u >>> car = 'Audi'
v >>> car.lower() == 'audi'
True
w >>> car
'Audi'

At u we assign the capitalized string 'Audi' to the variable car. At v
we convert the value of car to lowercase and compare the lowercase value
to the string 'audi'. The two strings match, so Python returns True. At w
we can see that the value stored in car has not been affected by the lower()
method.

Websites enforce certain rules for the data that users enter in a
manner similar to this. For example, a site might use a conditional test
like this to ensure that every user has a truly unique username, not just a
variation on the capitalization of another person’s username. When someone
submits a new username, that new username is converted to lowercase
and compared to the lowercase versions of all existing usernames. During
this check, a username like 'John' will be rejected if any variation of 'john'
is already in use.

p. 74 Checking for Inequality

When you want to determine whether two values are not equal, you can
combine an exclamation point and an equal sign (!=). The exclamation
point represents not, as it does in many programming languages.

p. 74-75 Numerical Comparisons

You can include various mathematical comparisons in your conditional
statements as well, such as less than, less than or equal to, greater than, and
greater than or equal to:

>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
Each mathematical comparison can be used as part of an if statement,
which can help you detect the exact conditions of interest.

p. 75-76 Using and to Check Multiple Conditions

To check whether two conditions are both True simultaneously, use the keyword
and to combine the two conditional tests; if each test passes, the overall
expression evaluates to True. If either test fails or if both tests fail, the
expression evaluates to False.

To improve readability, you can use parentheses around the individual
tests, but they are not required. If you use parentheses, your test would look
like this:

(age_0 >= 21) and (age_1 >= 21)

p. 76 Using or to Check Multiple Conditions

The keyword or allows you to check multiple conditions as well, but it
passes when either or both of the individual tests pass. An or expression
fails only when both individual tests fail.

p. 76-77 Checking Whether a Value IS in a List

To find out whether a particular value is already in a list, use the keyword
in.

requested_toppings = ['mushrooms', 'onions', 'pineapple']
u >>> 'mushrooms' in requested_toppings
True
v >>> 'pepperoni' in requested_toppings
False

At u and v, the keyword in tells Python to check for the existence of
'mushrooms' and 'pepperoni' in the list requested_toppings. This technique is
quite powerful because you can create a list of essential values, and then
easily check whether the value you’re testing matches one of the values in
the list.

p. 77 Checking Whether a Value Is Not in a List

Other times, it’s important to know if a value does not appear in a list. You
can use the keyword not in this situation.

banned_users = ['andrew', 'carolina', 'david']
_users.py user = 'marie'
u if user not in banned_users:
print(f"{user.title()}, you can post a response if you wish.")

The line at u reads quite clearly. If the value of user is not in the list
banned_users, Python returns True and executes the indented line.
The user 'marie' is not in the list banned_users, so she sees a message
inviting her to post a response:

Marie, you can post a response if you wish.

p. 77 Boolean Expressions

As you learn more about programming, you’ll hear the term Boolean
expression at some point. A Boolean expression is just another name for a
conditional test. A Boolean value is either True or False, just like the value
of a conditional expression after it has been evaluated.

Boolean values are often used to keep track of certain conditions, such
as whether a game is running or whether a user can edit certain content on
a website:

game_active = True
can_edit = False

Boolean values provide an efficient way to track the state of a program
or a particular condition that is important in your program.

p. 78-79 if Statements

When you understand conditional tests, you can start writing if statements.
Several different kinds of if statements exist, and your choice of which to
use depends on the number of conditions you need to test. You saw several
examples of if statements in the discussion about conditional tests, but now
let’s dig deeper into the topic.

p. 78-79 Simple if Statements

The simplest kind of if statement has one test and one action:

if conditional_test:
    do something

You can put any conditional test in the first line and just about any
action in the indented block following the test. If the conditional test
evaluates to True, Python executes the code following the if statement.
If the test evaluates to False, Python ignores the code following the if
statement.

Let’s say we have a variable representing a person’s age, and we want to
know if that person is old enough to vote. The following code tests whether
the person can vote:

voting.py

age = 19 u
if age >= 18: v
    print("You are old enough to vote!")

At u Python checks to see whether the value of age is greater than or
equal to 18. It is, so Python executes the indented print() call at v:
You are old enough to vote!

Indentation plays the same role in if statements as it did in for loops.
All indented lines after an if statement will be executed if the test passes,
and the entire block of indented lines will be ignored if the test does
not pass.

If the value of age is less than 18, this program would produce no
output.

p. 79-80 if-else Statements

An if-else block is similar to a simple if statement, but the else statement
allows you to define an action or set of actions that are executed when the
conditional test fails.


age = 17

if age >= 18: u
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

else: v
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

If the conditional test at u passes, the first block of indented print()
calls is executed. If the test evaluates to False, the else block at v is
executed. Because age is less than 18 this time, the conditional test fails and
the code in the else block is executed:
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!

This code works because it has only two possible situations to evaluate:
a person is either old enough to vote or not old enough to vote. The if-else
structure works well in situations in which you want Python to always execute
one of two possible actions. In a simple if-else chain like this, one of the two
actions will always be executed.

p. 80 The if-elif-else Chain

Often, you’ll need to test more than two possible situations, and to evaluate
these you can use Python’s if-elif-else syntax. Python executes only one
block in an if-elif-else chain. It runs each conditional test in order until
one passes. When a test passes, the code following that test is executed and
Python skips the rest of the tests.

amusement_park.py

age = 12

if age < 4: u
    print("Your admission cost is $0.")
elif age < 18: v
    print("Your admission cost is $25.")
else: w
    print("Your admission cost is $40.")

The if test at u tests whether a person is under 4 years old. If the test
passes, an appropriate message is printed and Python skips the rest of the
tests. The elif line at v is really another if test, which runs only if the
previous test failed. At this point in the chain, we know the person is at least
4 years old because the first test failed. If the person is under 18, an
appropriate message is printed and Python skips the else block. If both the if
and elif tests fail, Python runs the code in the else block at w.

In this example the test at u evaluates to False, so its code block is not
executed. However, the second test evaluates to True (12 is less than 18) so
its code is executed. The output is one sentence, informing the user of the
admission cost:

Your admission cost is $25.

Any age greater than 17 would cause the first two tests to fail. In these
situations, the else block would be executed and the admission price would
be $40.

Rather than printing the admission price within the if-elif-else block,
it would be more concise to set just the price inside the if-elif-else chain
and then have a simple print() call that runs after the chain has been
evaluated:

age = 12

if age < 4:
    price = 0 u
elif age < 18:
    price = 25 v
else:
    price = 40 w

print(f"Your admission cost is ${price}.") x

The lines at u, v, and w set the value of price according to the person’s
age, as in the previous example. After the price is set by the if-elif-else chain,
a separate unindented print() call  uses this value to display a message
reporting the person’s admission price.

This code produces the same output as the previous example, but the
purpose of the if-elif-else chain is narrower. Instead of determining a
price and displaying a message, it simply determines the admission price.
In addition to being more efficient, this revised code is easier to modify
than the original approach. To change the text of the output message,
you would need to change only one print() call rather than three separate
print() calls.

p. 81 - Using Multiple elif Blocks

You can use as many elif blocks in your code as you like. Let’s say that anyone
65 or older pays half the regular admission, or $20:

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65: u
    price = 40

else:
    price = 20 v

print(f"Your admission cost is ${price}.")

Most of this code is unchanged. The second elif block at u now checks
to make sure a person is less than age 65 before assigning them the full
admission rate of $40. Notice that the value assigned in the else block at v
needs to be changed to $20, because the only ages that make it to this block
are people 65 or older.

p. 82-83 Omitting the else Block

Python does not require an else block at the end of an if-elif chain. Sometimes
an else block is useful; sometimes it is clearer to use an additional
elif statement that catches the specific condition of interest:

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65:
    price = 20 u

print(f"Your admission cost is ${price}.")

The extra elif block at u assigns a price of $20 when the person is 65
or older, which is a bit clearer than the general else block. With this change,
every block of code must pass a specific test in order to be executed.

The else block is a catchall statement. It matches any condition that
wasn’t matched by a specific if or elif test, and that can sometimes include
invalid or even malicious data. If you have a specific final condition you are
testing for, consider using a final elif block and omit the else block. As a
result, you’ll gain extra confidence that your code will run only under the
correct conditions.

p. 83 Testing Multiple Conditions

However, sometimes it’s important to check all of the conditions of
interest. In this case, you should use a series of simple if statements with no
elif or else blocks. This technique makes sense when more than one condition
could be True, and you want to act on every condition that is True.
Let’s reconsider the pizzeria example. If someone requests a two-topping
pizza, you’ll need to be sure to include both toppings on their pizza:

toppings.py

requested_toppings = ['mushrooms', 'extra cheese'] u

if 'mushrooms' in requested_toppings: v
    print("Adding mushrooms.")


if 'pepperoni' in requested_toppings: w
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings: x
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

We start at u with a list containing the requested toppings. The if
statement at v checks to see whether the person requested mushrooms
on their pizza. If so, a message is printed confirming that topping. The
test for pepperoni at w is another simple if statement, not an elif or else
statement, so this test is run regardless of whether the previous test passed
or not. The code at x checks whether extra cheese was requested regardless
of the results from the first two tests. These three independent tests
are executed every time this program is run.

Because every condition in this example is evaluated, both mushrooms
and extra cheese are added to the pizza:

Adding mushrooms.
Adding extra cheese.

Finished making your pizza!


This code would not work properly if we used an if-elif-else block,
because the code would stop running after only one test passes. Here’s what
that would look like:

requested_toppings = ['mushrooms', 'extra cheese'] u

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")


elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

else 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

The test for 'mushrooms' is the first test to pass, so mushrooms are added
to the pizza. However, the values 'extra cheese' and 'pepperoni' are never
checked, because Python doesn’t run any tests beyond the first test that
passes in an if-elif-else chain. The customer’s first topping will be added,
but all of their other toppings will be missed:

Adding mushrooms.

Finished making your pizza!

In summary, if you want only one block of code to run, use an if-elif-else
chain. If more than one block of code needs to run, use a series of
independent if statements.

p. 85-86 Using if Statements with Lists

p. 86-87 Checking for Special Items

understand this already

u requested_toppings = []

if requested_toppings: v
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else: w
    print("Are you sure you want a plain pizza?")

This time we start out with an empty list of requested toppings at u.
Instead of jumping right into a for loop, we do a quick check at v. When the
name of a list is used in an if statement, Python returns True if the list
contains at least one item; an empty list evaluates to False. If
requested_toppings passes the conditional test, we run the same for loop we
used in the previous example. If the conditional test fails, we print a message
asking the customer if they really want a plain pizza with no toppings w.
The list is empty in this case, so the output asks

p. 88-89 Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese'] u

requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] v

for requested_topping in requested_toppings: w
    if requested_topping in available_toppings: x
        print(f"Adding {requested_topping}.")
    else: y
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

At u we define a list of available toppings at this pizzeria. Note that
this could be a tuple if the pizzeria has a stable selection of toppings. At v,
we make a list of toppings that a customer has requested. Note the unusual
request, 'french fries'. At w we loop through the list of requested toppings.
Inside the loop, we first check to see if each requested topping is actually
in the list of available toppings x. If it is, we add that topping to the pizza.
If the requested topping is not in the list of available toppings, the else
block will run y. The else block prints a message telling the user which
toppings are unavailable.

Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!

p. 90 Styling Your if Statements
In every example in this chapter, you’ve seen good styling habits. The only
recommendation PEP 8 provides for styling conditional tests is to use a
single space around comparison operators, such as ==, >=, <=. For example:

if age < 4:

is better than:

if age<4:

Such spacing does not affect the way Python interprets your code; it just
makes your code easier for you and others to read.

'''
