import math

# p. 51 6.1 Return Values

'''
In this chapter, we are (finally) going to write fruitful functions. The first example is area,
which returns the area of a circle with the given radius:

def area(radius):
    a = math.pi * radius**2
    return a

We have seen the return statement before, but in a fruitful function the return statement
includes an expression. This statement means: “Return immediately from this function
and use the following expression as a return value.”

The expression can be arbitrarily
complicated, so we could have written this function more concisely:

def area(radius):
    return math.pi * radius**2

On the other hand, temporary variables like a can make debugging easier.

Sometimes it is useful to have multiple return statements, one in each branch of a conditional:

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

Since these return statements are in an alternative conditional, only one runs.

As soon as a return statement runs, the function terminates without executing any subsequent
statements. Code that appears after a return statement, or any other place the flow
of execution can never reach, is called dead code.

As an exercise, write a compare function that takes two values, x and y, and returns 1 if x
> y, 0 if x == y, and -1 if x < y.



def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return 1


print(compare(5, 0))

p. 52-54 6.2 Incremental development

To deal with increasingly complex programs, you might want to try a process called incremental
development. The goal of incremental development is to avoid long debugging
sessions by adding and testing only a small amount of code at a time.

The final version of the function doesn’t display anything when it runs; it only returns
a value. The print statements we wrote are useful for debugging, but once you get the
function working, you should remove them. Code like that is called scaffolding because it
is helpful for building the program but is not part of the final product.

When you start out, you should add only a line or two of code at a time. As you gain more
experience, you might find yourself writing and debugging bigger chunks. Either way,
incremental development can save you a lot of debugging time.
The key aspects of the process are:

1. Start with a working program and make small incremental changes. At any point, if
there is an error, you should have a good idea where it is.

2. Use variables to hold intermediate values so you can display and check them.

3. Once the program is working, you might want to remove some of the scaffolding or
consolidate multiple statements into compound expressions, but only if it does not
make the program difficult to read.


# hypotenuse exercise c = √ (a**2 + b**2)


def hypotenuse(a, b):
    return 0.0


# print(hypotenuse(2, 4, 6))


def hypotenuse(a, b):
    c = a + b
    print('c is', c)
    return 0.0

# print(hypotenuse(2, 4, 6))


def hypotenuse(a, b):
    c = a + b
    csquared = a**2 + b**2
    print('csquared is:', csquared)
    return 0.0


# print(hypotenuse(2, 4, 6))

def hypotenuse(a, b):
    c = a + b
    csquared = a**2 + b**2
    result = math.sqrt(csquared)
    return result


print(hypotenuse(2, 8))

# p. 54 6.3 Composition

Assume that the center point is stored in the variables xc and yc, and the perimeter point is
in xp and yp. The first step is to find the radius of the circle, which is the distance between
the two points. We just wrote a function, distance, that does that:

radius = distance(xc, yc, xp, yp)

The next step is to find the area of a circle with that radius; we just wrote that, too:

result = area(radius)

Encapsulating these steps in a function, we get:


def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


The temporary variables radius and result are useful for development and debugging,
but once the program is working, we can make it more concise by composing the function
calls:


def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


p. 54-55 Boolean functions

It is common to give boolean functions names that sound like yes/no questions;
is_divisible returns either True or False to indicate whether x is divisible by y.
Here is an example:

>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True

Boolean functions are often used in conditional statements:
if is_divisible(x, y):
    print('x is divisible by y')

It might be tempting to write something like:
if is_divisible(x, y) == True:
    print('x is divisible by y')

But the extra comparison is unnecessary.

Exercise - write function that returns true if y is between x and z and false if otherwise.



def is_between(x, y, z):
    return x <= y <= z
    if is_between(x, y, z):
        return is_between()


print(is_between(5, 4, 4))

p. 55 6.5 More recursion

We have only covered a small subset of Python, but you might be interested to know that
this subset is a complete programming language, which means that anything that can be
computed can be expressed in this language.

A recursive definition is similar to a circular definition, in the sense that the
definition contains a reference to the thing being defined.

0! = 1
n! = n(n - 1)!

If you can write a recursive definition of something, you can write a Python program to
evaluate it. The first step is to decide what the parameters should be. In this case it should
be clear that factorial takes an integer:

def factorial(n):

If the argument happens to be 0, all we have to do is return 1:

def factorial(n):
    if n == 0:
        return 1

Otherwise, and this is the interesting part, we have to make a recursive call to find the
factorial of n 􀀀 1 and then multiply it by n:

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

If the factorial was 3:

Since 3 is not 0, we take the second branch and calculate the factorial of n-1...
Since 2 is not 0, we take the second branch and calculate the factorial of n-1...
Since 1 is not 0, we take the second branch and calculate the factorial
of n-1...
Since 0 equals 0, we take the first branch and return 1 without
making any more recursive calls.
The return value, 1, is multiplied by n, which is 1, and the result is
returned.
The return value, 1, is multiplied by n, which is 2, and the result is returned.

The return value (2) is multiplied by n, which is 3, and the result, 6, becomes the return
value of the function call that started the whole process.

p. 57 Leap of faith

When you come to a function call, instead of following the flow of execution, you
assume that the function works correctly and returns the right result.

p. 57-58 6.7 One more example

After factorial, the most common example of a recursively defined mathematical function
is fibonacci, which has the following definition (see http://en.wikipedia.org/
wiki/Fibonacci_number):
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n 􀀀 1) + fibonacci(n 􀀀 2)

Translated into Python, it looks like this:

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

6.8 Checking types

We can use the built-in function isinstance to verify the type of the argument. While
we’re at it, we can also make sure the argument is positive:

def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

The first base case handles nonintegers; the second handles negative integers. In both
cases, the program prints an error message and returns None to indicate that something
went wrong:

>>> print(factorial('fred'))
Factorial is only defined for integers.
None
>>> print(factorial(-2))
Factorial is not defined for negative integers.
None

This program demonstrates a pattern sometimes called a guardian. The first two conditionals
act as guardians, protecting the code that follows from values that might cause an
error. The guardians make it possible to prove the correctness of the code.

Breaking a large program into smaller functions creates natural checkpoints for debugging.
If a function is not working, there are three possibilities to consider:

• There is something wrong with the arguments the function is getting; a precondition
is violated.
• There is something wrong with the function; a postcondition is violated.
• There is something wrong with the return value or the way it is being used.

Adding print statements at the beginning and end of a function can help make the flow of
execution more visible. For example, here is a version of factorial with print statements:



def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result


space is a string of space characters that controls the indentation of the output.

print(factorial(5))

If you are confused about the flow of execution, this kind of output can be helpful. It takes
some time to develop effective scaffolding, but a little bit of scaffolding can save a lot of
debugging.

'''
