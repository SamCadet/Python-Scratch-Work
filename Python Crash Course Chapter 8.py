'''
p. 129 Chapter 8 Functions

In this chapter you’ll learn to write functions, which are named blocks of code
that are designed to do one specific job. When you want to perform a particular
task that you’ve defined in a function, you call the function responsible for
it.

p. 130 Defining a Function

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

This example shows the simplest structure of a function. The line at u
uses the keyword def to inform Python that you’re defining a function. This
is the function definition, which tells Python the name of the function and, if
applicable, what kind of information the function needs to do its job. The
parentheses hold that information. In this case, the name of the function
is greet_user(), and it needs no information to do its job, so its parentheses
are empty. (Even so, the parentheses are required.) Finally, the definition
ends in a colon.

This function just prints 'Hello!' anytime it's called and doesn't take any
arguments in parentheses. Don't forget to indent underneath the function
definition.

When you want to use this function, you call it. A function call tells
Python to execute the code in the function. To call a function, you write
the name of the function, followed by any necessary information in parentheses

p. 130-131

Passing Information to a Function

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

This is an example of passing an argument 'jesse' in a function to substitute
the parameter 'username' in greet_user(username.) When greet_user('jesse') gets
called, Python prints Hello, Jesse. Not including an argument in this case would
produce an error since python expects at least one.

p. 131 Arguments and Parameters

The variable username in the definition of greet_user() is an example of a
parameter, a piece of information the function needs to do its job. The value
'jesse' in greet_user('jesse') is an example of an argument. An argument
is a piece of information that’s passed from a function call to a function.

p. 131-132 Passing Arguments

You can use positional arguments, which need to be in the same order the
parameters were written; keyword arguments, where each argument consists of a
variable name and a value; and lists and dictionaries of values. Let’s look at
each of these in turn.

p. 132 Positional Arguments

When you call a function, Python must match each argument in the function
call with a parameter in the function definition. The simplest way to
do this is based on the order of the arguments provided. Values matched
up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

This function just substitutes the arguments for their respective parameters
in order to line up with the variables in each print statement. The parameters
are descriptive enough to show what types of words you need to enter i.e. a
type of animal and its name.

p. 132-133 Multiple Function Calls

describe_pet('dog', 'willie')

This is an example of calling a function more than once to describe a different
pet. The positional arguments still line up.

Calling a function multiple times is a very efficient way to work. The
code describing a pet is written once in the function. Then, anytime you
want to describe a new pet, you call the function with the new pet’s information.
Even if the code for describing a pet were to expand to ten lines,
you could still describe a new pet in just one line by calling the function
again.

You can use as many positional arguments as you need in your functions.
Python works through the arguments you provide when calling the
function and matches each one with the corresponding parameter in
the function’s definition.

p. 133 Order Matters in Positional Arguments

describe_pet('harry', 'hamster')

In this function call we list the name first and the type of animal second.
Because the argument 'harry' is listed first this time, that value is assigned
to the parameter animal_type. Likewise, 'hamster' is assigned to pet_name. Now
we have a “harry” named “Hamster”:

I have a harry.
My harry's name is Hamster.

If you get funny results like this, check to make sure the order of the
arguments in your function call matches the order of the parameters in the
function’s definition.

p. 133-134 Keyword Arguments
A keyword argument is a name-value pair that you pass to a function. You
directly associate the name and the value within the argument, so when you
pass the argument to the function, there’s no confusion (you won’t end up
with a harry named Hamster). Keyword arguments free you from having
to worry about correctly ordering your arguments in the function call, and
they clarify the role of each value in the function call.

describe_pet(animal_type='hamster', pet_name='harry')

The function describe_pet() hasn’t changed. But when we call the function,
we explicitly tell Python which parameter each argument should be
matched with. When Python reads the function call, it knows to assign the
argument 'hamster' to the parameter animal_type and the argument 'harry'
to pet_name. The output correctly shows that we have a hamster named
Harry.

The order of keyword arguments doesn’t matter because Python
knows where each value should go. The following two function calls are
equivalent:

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

Note When you use keyword arguments, be sure to use the exact names of the
parameters in the function’s definition.

p. 134 Default Values

When writing a function, you can define a default value for each parameter.
If an argument for a parameter is provided in the function call, Python uses
the argument value. If not, it uses the parameter’s default value. So when
you define a default value for a parameter, you can exclude the corresponding
argument you’d usually write in the function call. Using default values
can simplify your function calls and clarify the ways in which your functions
are typically used.

For example, if you notice that most of the calls to describe_pet() are
being used to describe dogs, you can set the default value of animal_type to
'dog'. Now anyone calling describe_pet() for a dog can omit that information:

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

We changed the definition of describe_pet() to include a default value,
'dog', for animal_type. Now when the function is called with no animal_type
specified, Python knows to use the value 'dog' for this parameter:

I have a dog.
My dog's name is Willie.

Note that the order of the parameters in the function definition had
to be changed. Because the default value makes it unnecessary to specify a
type of animal as an argument, the only argument left in the function call
is the pet’s name. Python still interprets this as a positional argument, so if
the function is called with just a pet’s name, that argument will match up
with the first parameter listed in the function’s definition. This is the reason
the first parameter needs to be pet_name.

The simplest way to use this function now is to provide just a dog’s
name in the function call:

describe_pet('willie')

This function call would have the same output as the previous example.
The only argument provided is 'willie', so it is matched up with the first
parameter in the definition, pet_name. Because no argument is provided for
animal_type, Python uses the default value 'dog'.

To describe an animal other than a dog, you could use a function call
like this:

describe_pet(pet_name='harry', animal_type='hamster')

Because an explicit argument for animal_type is provided, Python will
ignore the parameter’s default value.

Note - When you use default values, any parameter with a default value needs to
be listed after all the parameters that don’t have default values. This allows
Python to continue interpreting positional arguments correctly.

p. 135 Equivalent Function Calls

Because positional arguments, keyword arguments, and default values can
all be used together, often you’ll have several equivalent ways to call a function.
Consider the following definition for describe_pet() with one default
value provided:

def describe_pet(pet_name, animal_type='dog'):

With this definition, an argument always needs to be provided for
pet_name, and this value can be provided using the positional or keyword
format. If the animal being described is not a dog, an argument for
animal_type must be included in the call, and this argument can also be
specified using the positional or keyword format.

All of the following calls would work for this function:

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

Each of these function calls would have the same output as the previous
examples.

Note - It doesn’t really matter which calling style you use. As long as your
function calls produce the output you want, just use the style you find easiest
to understand.

Unmatched arguments occur when you provide fewer or more arguments than a
function needs to do its work.

describe_pet()

Would give us an error because the function asked for two arguments when you
provide any when it was called.

Traceback (most recent call last):
    File "pets.py", line 6, in <module>
        describe_pet()
TypeError: describe_pet() missing 2 required positional arguments: 'animal_
type' and 'pet_name'

Python is helpful in that it reads the function’s code for us and tells us
the names of the arguments we need to provide. This is another motivation
for giving your variables and functions descriptive names. If you do,
Python’s error messages will be more useful to you and anyone else who
might use your code.

If you provide too many arguments, you should get a similar traceback
that can help you correctly match your function call to the function
definition.

p. 137

The value the function returns is called a return value. The return statement
takes a value from inside a function and sends it back to the line that called
the function. Return values allow you to move much of your program’s grunt work
into functions, which can simplify the body of your program.

p. 138 Returning a Simple Value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

This function takes the parameters, turns them into a variable and then the
return statement produces the full name.

After that, the variable 'musician' gets the value of the function with
'jimi' and 'hendrix' as parameters. Finally the program prints musician to
display the output from the get_formatted_name function.

When you call a function that returns a value, you need to provide a
variable that the return value can be assigned to...or you can just use the
print function as shown below.



def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


print(get_formatted_name('jimi', 'hendrix'))

The output stays the same for either option

Jimi Hendrix

This might seem like a lot of work to get a neatly formatted name when
we could have just written:

print("Jimi Hendrix")

But when you consider working with a large program that needs to
store many first and last names separately, functions like get_formatted_name()
become very useful. You store first and last names separately and then call
this function whenever you want to display a full name.

p. 138 Making an Argument Optional

To make get_formatted_name() work without a middle name, we set the
default value of middle_name to an empty string and move it to the end of the
list of parameters:

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')

Just make the optional argument the last parameter and give it an empty string.
Make the code reflect both cases where a middle name would and wouldn't be
included as such above with an if-else statement for example.

If you want to add the optional argument, put it at the end of the function
call. You have to match the positions of each name correctly or else the
function won't work.

Optional values allow functions to handle a wide range of use cases
while letting function calls remain as simple as possible.

p. 140 Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

{'first': 'jimi', 'last': 'hendrix'}

Pretty self explanatory, just format the variable 'person' as a dictionary
and use return to produce the diciontary whenever the function gets called...

You can easily extend this function to accept
optional values like a middle name, an age, an occupation, or any other
information you want to store about a person. For example, the following
change allows you to store a person’s age as well:

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

We add a new optional parameter age to the function definition and
assign the parameter the special value None, which is used when a variable
has no specific value assigned to it. You can think of None as a placeholder
value. In conditional tests, None evaluates to False. If the function call
includes a value for age, that value is stored in the dictionary. This function
always stores a person’s name, but it can also be modified to store any other
information you want about a person.

p. 141 Using a Function with a while Loop


Where do you put a quit condition when you ask for a series of
inputs? We want the user to be able to quit as easily as possible, so each
prompt should offer a way to quit. The break statement offers a straightforward
way to exit the loop at either prompt:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
    break

    l_name = input("Last name: ")
    if l_name == 'q':
    break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

We add a message that informs the user how to quit, and then we
break out of the loop if the user enters the quit value at either prompt.
Now the program will continue greeting people until someone enters 'q'
for either name:

Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit)
First name: q

p. 143 Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

We define greet_users() so it expects a list of names, which it assigns
to the parameter names. The function loops through the list it receives and
prints a greeting to each user. At u we define a list of users and then pass
the list usernames to greet_users() in our function call:

Hello, Hannah!
Hello, Ty!
Hello, Margot!

p. 143-144 Modifying a List in a Function

We can reorganize this code by writing two functions, each of which
does one specific job. Most of the code won’t change; we’re just making
it more carefully structured. The first function will handle printing the
designs, and the second will summarize the prints that have been made:

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

At u we define the function print_models() with two parameters: a list of
designs that need to be printed and a list of completed models. Given these
two lists, the function simulates printing each design by emptying the list
of unprinted designs and filling up the list of completed models. At v we
define the function show_completed_models() with one parameter: the list of
completed models. Given this list, show_completed_models() displays the name
of each model that was printed.

This program has the same output as the version without functions, but
the code is much more organized. The code that does most of the work has
been moved to two separate functions, which makes the main part of the
program easier to understand. Look at the body of the program to see how
much easier it is to understand what this program is doing:

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

This program is easier to extend and maintain than the version without
functions. If we need to print more designs later on, we can simply call
print_models() again. If we realize the printing code needs to be modified,
we can change the code once, and our changes will take place everywhere
the function is called. This technique is more efficient than having to update
code separately in several places in the program.

This example also demonstrates the idea that every function should
have one specific job. The first function prints each design, and the second
displays the completed models. This is more beneficial than using one function
to do both jobs. If you’re writing a function and notice the function
is doing too many different tasks, try to split the code into two functions.
Remember that you can always call a function from another function,
which can be helpful when splitting a complex task into a series of steps.

p. 145 Preventing a Function from Modifying a List

You can send a copy of a list to a function like this:

function_name(list_name[:])

The slice notation [:] makes a copy of the list to send to the function.
If we didn’t want to empty the list of unprinted designs in printing_models.py,
we could call print_models() like this:

print_models(unprinted_designs[:], completed_models)

The slice notation [:] makes a copy of the list to send to the function.
If we didn’t want to empty the list of unprinted designs in printing_models.py,
we could call print_models() like this:

print_models(unprinted_designs[:], completed_models)

The function print_models() can do its work because it still receives the
names of all unprinted designs. But this time it uses a copy of the original
unprinted designs list, not the actual unprinted_designs list. The list
completed_models will fill up with the names of printed models like it did
before, but the original list of unprinted designs will be unaffected by the
function.

Even though you can preserve the contents of a list by passing a copy
of it to your functions, you should pass the original list to functions unless
you have a specific reason to pass a copy. It’s more efficient for a function
to work with an existing list to avoid using the time and memory needed to
make a separate copy, especially when you’re working with large lists.

p. 147 Passing an Arbitrary Number of Arguments

The function in the following example has one parameter,
*toppings, but this parameter collects as many arguments as the calling
line provides:

pizza.py

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

The asterisk in the parameter name *toppings tells Python to make an
empty tuple called toppings and pack whatever values it receives into this
tuple. The print() call in the function body produces output showing that
Python can handle a function call with one value and a call with three
values. It treats the different calls similarly. Note that Python packs the
arguments into a tuple, even if the function receives only one value:

Now we can replace the print() call with a loop that runs through the
list of toppings and describes the pizza being ordered:

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

The function responds appropriately, whether it receives one value or
three values:

Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

This syntax works no matter how many arguments the function
receives.

p. 148 Mixing Positional and Arbitrary Arguments

If you want a function to accept several different kinds of arguments, the
parameter that accepts an arbitrary number of arguments must be placed
last in the function definition. Python matches positional and keyword
arguments first and then collects any remaining arguments in the final
parameter.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

In the function definition, Python assigns the first value it receives to
the parameter size. All other values that come after are stored in the tuple
toppings. The function calls include an argument for the size first, followed
by as many toppings as needed.

Now each pizza has a size and a number of toppings, and each piece of
information is printed in the proper place, showing size first and toppings
after:

Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

Note - You’ll often see the generic parameter name *args, which collects
arbitrary positional arguments like this.

p.149 Using Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first u
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)

The definition of build_profile() expects a first and last name, and
then it allows the user to pass in as many name-value pairs as they want. The
double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs
it receives into this dictionary. Within the function, you can access the keyvalue
pairs in user_info just as you would for any dictionary.

In the body of build_profile(), we add the first and last names to the
user_info dictionary because we’ll always receive these two pieces of information
from the user u, and they haven’t been placed into the dictionary
yet. Then we return the user_info dictionary to the function call line.

We call build_profile(), passing it the first name 'albert', the last
name 'einstein', and the two key-value pairs location='princeton' and
field='physics'. We assign the returned profile to user_profile and print
user_profile

{'location': 'princeton', 'field': 'physics',
'first_name': 'albert', 'last_name': 'einstein'}

The returned dictionary contains the user’s first and last names and,
in this case, the location and field of study as well. The function would
work no matter how many additional key-value pairs are provided in the
function call.

For now, remember to use the simplest approach that gets the job done. As you
progress you’ll learn to use the most efficient approach each time.

Note - You’ll often see the parameter name **kwargs used to collect
non-specific keyword arguments.

P. 150 Storing Your Functions in Modules

You can go a step further by
storing your functions in a separate file called a module and then importing
that module into your main program. An import statement tells Python to
make the code in a module available in the currently running program file.

p. 150-151 Importing an Entire Module

A module is a file ending in .py that contains the code you want to import into
your program.

To
make this module, we’ll remove everything from the file pizza.py except the
function make_pizza():

pizza.py

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

Now we’ll make a separate file called making_pizzas.py in the same
directory as pizza.py. This file imports the module we just created and then
makes two calls to make_pizza():
making_pizzas.py

import pizza

pizza.make_pizza(16, 'pepperoni') u
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

file pizza.py and copy all the functions from it into this program. You
don’t actually see code being copied between files because Python copies
the code behind the scenes just before the program runs. All you need
to know is that any function defined in pizza.py will now be available in
making_pizzas.py.

To call a function from an imported module, enter the name of
the module you imported, pizza, followed by the name of the function,
make_pizza(), separated by a dot u. This code produces the same output
as the original program that didn’t import a module:

This first approach to importing, in which you simply write import followed
by the name of the module, makes every function from the module
available in your program. If you use this kind of import statement to import
an entire module named module_name.py, each function in the module is
available through the following syntax:
module_name.function_name()

Importing Specific Functions p. 152
from module_name import function_name
from module_name import function_0, function_1, function_2

The making_pizzas.py example would look like this if we want to import
just the function we’re going to use:

from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

With this syntax, you don’t need to use the dot notation when you call a
function. Because we’ve explicitly imported the function make_pizza() in the
import statement, we can call it by name when we use the function.


p. 152 Using as to Give a Function an Alias

If the name of a function you’re importing might conflict with an existing
name in your program or if the function name is long, you can use a
short, unique alias—an alternate name similar to a nickname for the function.
You’ll give the function this special nickname when you import the
function.

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

The general syntax for providing an alias is:

from module_name import function_name as fn

p. 153 Using as to Give a Module an Alias

You can also provide an alias for a module name. Giving a module a short
alias, like p for pizza, allows you to call the module’s functions more quickly.
Calling p.make_pizza() is more concise than calling pizza.make_pizza():

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

The module pizza is given the alias p in the import statement, but all of
the module’s functions retain their original names. Calling the functions by
writing p.make_pizza() is not only more concise than writing pizza.make_pizza(),
but also redirects your attention from the module name and allows you
to focus on the descriptive names of its functions. These function names,
which clearly tell you what each function does, are more important to the
readability of your code than using the full module name.

The general syntax for this approach is:

import module_name as mn

Importing All Functions in a Module
You can tell Python to import every function in a module by using the asterisk
(*) operator:

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

The asterisk in the import statement tells Python to copy every function
from the module pizza into this program file. Because every function
is imported, you can call each function by name without using the dot
notation. However, it’s best not to use this approach when you’re working
with larger modules that you didn’t write: if the module has a function
name that matches an existing name in your project, you can get some
unexpected results. Python may see several functions or variables with the
same name, and instead of importing all the functions separately, it will
overwrite the functions.

The best approach is to import the function or functions you want,
or import the entire module and use the dot notation. This leads to clear
code that’s easy to read and understand. I include this section so you’ll
recognize import statements like the following when you see them in other
people’s code:

from module_name import *

p. 154 Styling Functions

Every function should have a comment that explains concisely what
the function does. This comment should appear immediately after the
function definition and use the docstring format. In a well-documented
function, other programmers can use the function by reading only the
description in the docstring. They should be able to trust that the code
works as described, and as long as they know the name of the function,
the arguments it needs, and the kind of value it returns, they should be
able to use it in their programs.

If you specify a default value for a parameter, no spaces should be used
on either side of the equal sign:

def function_name(parameter_0, parameter_1='default value')

The same convention should be used for keyword arguments in function
calls:

function_name(value_0, parameter_1='value')

PEP 8 (https://www.python.org/dev/peps/pep-0008/ ) recommends that
you limit lines of code to 79 characters so every line is visible in a reasonably
sized editor window. If a set of parameters causes a function’s definition to
be longer than 79 characters, press enter after the opening parenthesis on
the definition line. On the next line, press tab twice to separate the list of
arguments from the body of the function, which will only be indented one
level.

Most editors automatically line up any additional lines of parameters to
match the indentation you have established on the first line:

def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...

All import statements should be written at the beginning of a file.
The only exception is if you use comments at the beginning of your file to
describe the overall program
'''
