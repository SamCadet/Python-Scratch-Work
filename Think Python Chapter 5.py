import time
import math
import turtle

# p. 39 5.1 Floor division and modulus

'''
The floor division operator, //, divides two numbers
and rounds down to an integer.

>>> minutes = 105
>>> hours = minutes // 60
>>> hours
1

the modulus operator, %, divides two numbers and returns
the remainder.

>>> remainder = minutes % 60
>>> remainder
45

# p. 40 5.2 Boolean expressions

A boolean expression is an expression that is either true or false.

>>> 5 == 5
True
>>> 5 == 6
False

# p. 40-41 5.3 Logical operators

There are three logical operators: and, or, and not. The semantics (meaning) of these
operators is similar to their meaning in English. For example, x > 0 and x < 10 is true
only if x is greater than 0 and less than 10.

n%2 == 0 or n%3 == 0 is true if either or both of the conditions is true, that is, if the number
is divisible by 2 or 3.

Finally, the not operator negates a boolean expression, so not (x > y) is true if x > y is
false, that is, if x is less than or equal to y.

# p. 41 5.4 Conditional execution

In order to write useful programs, we almost always need the ability to check conditions
and change the behavior of the program accordingly. Conditional statements give us this
ability. The simplest form is the if statement:

if x > 0:
    print('x is positive')

The boolean expression after if is called the condition. If it is true, the indented statement
runs. If not, nothing happens.

Occasionally, it is useful to have a body with no statements (usually as a
place keeper for code you haven’t written yet). In that case, you can use the pass statement,
which does nothing.

if x < 0:
    pass # TODO: need to handle negative values!

# p. 41 Alternative execution

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

If the remainder when x is divided by 2 is 0, then we know that x is even, and the program
displays an appropriate message. If the condition is false, the second set of statements
runs. Since the condition must be true or false, exactly one of the alternatives will run. The
alternatives are called branches, because they are branches in the flow of execution.

# p. 41-42 Chained conditionals

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

elif is an abbreviation of “else if”. Again, exactly one branch will run. There is no limit on
the number of elif statements. If there is an else clause, it has to be at the end, but there
doesn’t have to be one.

if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()

Even if more than one condition is true, only the first true branch runs.

p. 42-43 5.7 Nested conditionals

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
else:
    print('x is greater than y')

Although the indentation of the statements makes the structure apparent, nested conditionals
become difficult to read very quickly. It is a good idea to avoid them when you
can.

Logical operators often provide a way to simplify nested conditional statements. For example,
we can rewrite the following code using a single conditional:
    if 0 < x:
        if x < 10:
            print('x is a positive single-digit number.')

The print statement runs only if we make it past both conditionals, so we can get the same
effect with the and operator:

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

For this kind of condition, Python provides a more concise option:

if 0 < x < 10:
    print('x is a positive single-digit number.')

p. 43-44 5.8 Recursion


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)


countdown(6)

A function that calls itself is recursive; the process of executing it is called recursion.
As another example, we can write a function that prints a string n times.



def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)


print_n(5, 8)


If n <= 0 the return statement exits the function. The flow of execution immediately returns
to the caller, and the remaining lines of the function don’t run.

The rest of the function is similar to countdown: it displays s and then calls itself to display
s n - 1 additional times. So the number of lines of output is 1 + (n - 1), which adds up
to n.

p. 44 5.9 Stack diagrams for recursive functions

As an exercise, draw a stack diagram for print_n called with s = 'Hello' and n=2. Then
write a function called do_n that takes a function object and a number, n, as arguments, and
that calls the given function n times.

def print_n('Helo, 2')

print_n(n isn't less than or equal to zero because it's a string)
    no return
print_n(print(s) means 'Hello gets printed')
print_n((s, n-1) 'Hello' gets printed 1 + 2 - 1 times == 'Hello' gets printed twice.


def do_n(x, n):
    if n <= 0:
        return
    print(x)
    do_n(x, n - 1)


do_n('Whoadie', 6)

p. 44 5.10 Infinite recursion

If a recursion never reaches a base case, it goes on making recursive calls forever, and the
program never terminates. This is known as infinite recursion, and it is generally not a
good idea.

def recurse():
    # This would keep calling itself until Python hits a RuntimeError.
    recurse()

If you encounter an infinite recursion by accident, review your function to confirm that
there is a base case that does not make a recursive call. And if there is a base case, check
whether you are guaranteed to reach it.

p. 45-6 5.11 Keyboard input

Before getting input from the user, it is a good idea to print a prompt telling the user what
to type. input can take a prompt as an argument:

>>> name = input('What...is your name?\n')
What...is your name?
Yung Wone!
>>> name
'Yung Wone!'

The sequence \n at the end of the prompt represents a newline, which is a special character
that causes a line break. That’s why the user’s input appears below the prompt.

If you expect the user to type an integer, you can try to convert the return value to int:
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
42
>>> int(speed)
42

But if the user types something other than a string of digits, you get an error:
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10

p. 46 5.12 Debugging

Syntax errors are usually easy to find, but there are a few gotchas. Whitespace errors can
be tricky because spaces and tabs are invisible and we are used to ignoring them.
>>> x = 5
>>>  y = 6
File "<stdin>", line 1
y = 6
^
IndentationError: unexpected indent

In this example, the problem is that the second line is indented by one space. But the error
message points to y, which is misleading. In general, error messages indicate where the
problem was discovered, but the actual error might be earlier in the code, sometimes on a
previous line.

p. 47 Exercise 5.1

currentTime = time.ctime()
time = time.time()
print(currentTime)
print(time)
print(time // 86400)

p. 48 Exercise 5.2


# 1. TODO: write a function named check_format for a, b, c, and n

def check_format(a, b, c, n):
    # TODO: check to see if a^n + b^n = c^n is true in function, has to be greater than 2
    # if n <= 2:
        # print('n has to be greater than 2, whoadie.')
        # return
    # TODO: make if statement that prints correct and incorrect scenarios
    if a**n + b**n == c**n:
        print('Ayo, Fermat was a buster!')
    else:
        print('Nah, that won\'t cut it, #myguy.')


check_format(3, 0, 3, 2)


# 2. input version - TODO: write a function named check_format for a, b, c, and n

def check_format():

    # TODO: check to see if a^n + b^n = c^n is true in function from user's input
    while True:
        a = input('Enter a value for a: ')
        b = input('Enter a value for b: ')
        c = input('Enter a value for c: ')
        n = input('Enter a value for n: ')
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            n = int(n)
        except:
            print('Please use numeric digits.')
            continue
        # TODO: make if statement that prints correct and incorrect scenarios
        if a**n + b**n == c**n:
            print('Ayo, Fermat was a buster!')
        else:
            print('Nah, that won\'t cut it, #myguy.')


check_format()



# p. 48 Exercise 5.3


# 1. TODO: write a function called is_triangle that takes three integers as arguments


def is_triangle(a, b, c):
    # TODO: check to see if one of the sides is greater than the sum of the other two sides
    if a and b and c < 1:
        print('Please enter positive numbers only')
        return

    if a or b or c > a + b and a + c and b + c:
        # TODO: print yes or no if you can form a triangle from the given lengths
        print('No triangle, whoadie')
    else:
        print('Gimme dat triangle!')

# TODO: run that function yooooooo


is_triangle(1, 1, -3)



# 2. input version - TODO: write a function called is_triangle that takes three integers as arguments


def is_triangle():
    # TODO: ask user to enter values for a, b, and c
    while True:
        a = input('Enter a value for a: ')
        b = input('Enter a value for b: ')
        c = input('Enter a value for c: ')
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            print('Please enter numeric digits only.')
            continue
        if a and b and c < 1:
            print('Please enter positive numbers only')
            continue
        if a or b or c > a + b and a + c and b + c:
            # TODO: print yes or no if you can form a triangle from the given lengths
            print('No triangle, whoadie')
        else:
            print('Gimme dat triangle!')

# TODO: run that function yooooooo


is_triangle()

# p. 48 Exercise 5.4


def recurse(n, s):  # sets instructions for two arguments n and s
    if n == 0:
        print(s)  # just prints s if n is zero
    else:  # for all other cases...
        # displays the difference of of n-1 and then calls itself to display n + s times times
        recurse(n - 1, n + s)
        # recurse(5,0) = (5-1, 5+0) s starts at 5 and keeps adding itself downwards
        # by subtracting one until it reaches 0, 5 + 4 + 3 + 2 + 1 = 15


recurse(5, 0)

# 1. It'd just be 1 since (1-1 = - and 1  + 0 just makes it repeat once)
# 2. You'd have to know that functions can call itself until it reaches 0




# p. 48-49 Exercise 5.5


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)


myGuy = turtle.Turtle()
draw(myGuy, 2, 8)

# It'll make inverted triangles, wrong, it's drawing some weird shit.

# p. 49 Exercise 5.6

'''

# TODO: draw this dumb ass shape

# Answer - https://github.com/AllenDowney/ThinkPython2/blob/master/code/koch.py

'''
Wrong answer, trash
def koch(t, n):
    for i in range(40):
        t.fd(length / 3)
        t.lt(60)
        t.fd(length / 3)
        t.rt(120)
        t.fd(length / 3)
        t.lt(60)
        t.fd(length / 3)


myGuy = turtle.Turtle()

koch(myGuy, 40)
'''
# real answer


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()
