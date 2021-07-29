import math

# Chapter 7 - Iteration

# p. 63 7.1 Reassignment

'''

As you may have discovered, it is legal to make more than one assignment to the same
variable. A new assignment makes an existing variable refer to a new value (and stop
referring to the old value).
>>> x = 5
>>> x
5
>>> x = 7
>>> x
7
The first time we display x, its value is 5; the second time, its value is 7.

#. p. 64 7.2 Updating Variables

A common kind of reassignment is an update, where the new value of the variable depends
on the old.
>>> x = x + 1
This means “get the current value of x, add one, and then update x with the new value.”

If you try to update a variable that doesn’t exist, you get an error, because Python evaluates
the right side before it assigns a value to x:
>>> x = x + 1
NameError: name 'x' is not defined
Before you can update a variable, you have to initialize it, usually with a simple assignment:
>>> x = 0
>>> x = x + 1
Updating a variable by adding 1 is called an increment; subtracting 1 is called a decrement.

p. 64 7.3 The while statement

In a computer program, repetition is also called iteration.

Python provides language features to make it easier. One
is the for statement we saw in Section 4.2. We’ll get back to that later.
Another is the while statement. Here is a version of countdown that uses a while statement:

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
print('Blastoff!')

You can almost read the while statement as if it were English. It means, “While n is greater
than 0, display the value of n and then decrement n. When you get to 0, display the word
Blastoff!”

More formally, here is the flow of execution for a while statement:
1. Determine whether the condition is true or false.
2. If false, exit the while statement and continue execution at the next statement.
3. If the condition is true, run the body and then go back to step 1.

This type of flow is called a loop because the third step loops back around to the top.

The body of the loop should change the value of one or more variables so that the condition
becomes false eventually and the loop terminates. Otherwise the loop will repeat forever,
which is called an infinite loop.



def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else:           # n is odd
            n = n * 3 + 1


sequence(3)




# 7.3 Exercise


def print_n(s, n):
    while n >= 0:
        print(n)
        print_n(s, n - 1)
        break


print_n(6, 2)

p. 66 7.4 break

Sometimes you don’t know it’s time to end a loop until you get half way through the body.
In that case you can use the break statement to jump out of the loop.


while True:
    line = input('> ')
    if line == 'done':
        break   # typing done as the input breaks the loop, otherwise, this function just repeats what you typed
    print(line)

print('We outta here, y\'all! PEACE!!!')

This way of writing while loops is common because you can check the condition anywhere
in the loop (not just at the top) and you can express the stop condition affirmatively (“stop
when this happens”) rather than negatively (“keep going until that happens”).


p. 66 7.5 Square roots

In general we don’t know ahead of time how many steps it takes to get to the right answer,
but we know when we get there because the estimate stops changing:
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0

When y == x, we can stop. Here is a loop that starts with an initial estimate, x, and improves
it until it stops changing:
while True:
    print(x)
    y = (x + a/x) / 2   # Newton's method to find the square root of a via an estimate x
    if y == x:
        break
    x = y


Rather than checking whether x and y are exactly equal, it is safer to use the built-in function
abs to compute the absolute value, or magnitude, of the difference between them:

if abs(y-x) < epsilon:
    break

p. 67-68 7.6 Algorithms

Newton’s method is an example of an algorithm: it is a mechanical process for solving a
category of problems (in this case, computing square roots).

But if you were “lazy”, you might have learned a few tricks. For example, to find the
product of n and 9, you can write n 􀀀 1 as the first digit and 10 􀀀 n as the second digit.
This trick is a general solution for multiplying any single-digit number by 9. That’s an
algorithm!

Similarly, the techniques you learned for addition with carrying, subtraction with borrowing,
and long division are all algorithms. One of the characteristics of algorithms is that they do not require any intelligence to carry out. They are mechanical processes where
each step follows from the last according to a simple set of rules.

p. 68 Debugging

One way to cut your debugging time is “debugging by bisection”. For example, if there
are 100 lines in your program and you check them one at a time, it would take 100 steps.

Instead, try to break the problem in half. Look at the middle of the program, or near it, for
an intermediate value you can check. Add a print statement (or something else that has a
verifiable effect) and run the program.

If the mid-point check is incorrect, there must be a problem in the first half of the program.
If it is correct, the problem is in the second half.

In practice it is not always clear what the “middle of the program” is and not always possible
to check it. It doesn’t make sense to count lines and find the exact midpoint. Instead,
think about places in the program where there might be errors and places where it is easy
to put a check. Then choose a spot where you think the chances are about the same that
the bug is before or after the check.

p. 69 7.9 Exercises


# TODO make a function called mysqrt that takes a as a parameter, a reasonable value
# of x and returns an estimate of the square root of a

# Answer - https://github.com/MadCzarls/Think-Python-2e---my-solutions/blob/master/ex7/ex7.1.py



def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y

# TODO: write a function named test_square_root that tests mysqrt with a table


def test_square_root(list_of_a):
    """Displays outcomes of calculating square root of a using different methods;
    list_of_a - list of positive digit.
    """
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"

    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"

    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""

    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)

    for a in list_of_a:
        col1 = (a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)


test_square_root(range(1, 10))

p. 69 Exercise 7.2. The built-in function eval takes a string and evaluates it using the Python interpreter.
'''

print(eval('1 + 2 * 3'))

'''
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated.

'''

# TODO: Write a function called eval_loop

# TODO: Make it run until the user enters done to return the value of the last expression
