import pyinputplus as pyip

# Chapter 8 - Input Validation

'''
p. 211-212

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

When you run this code, you’ll be prompted for your age until you
enter a valid one. This ensures that by the time the execution leaves the
while loop, the age variable will contain a valid value that won’t crash the
program later on.

p. 212-214 The PyInputPlus Module

PyInputPlus contains functions similar to input() for several kinds of
data: numbers, dates, email addresses, and more.

inputStr() Is like the built-in input() function but has the general
PyInputPlus features. You can also pass a custom validation function
to it

inputNum() Ensures the user enters a number and returns an int or
float, depending on if the number has a decimal point in it

inputChoice() Ensures the user enters one of the provided choices

inputMenu() Is similar to inputChoice(), but provides a menu with
numbered or lettered options

inputDatetime() Ensures the user enters a date and time

inputYesNo() Ensures the user enters a “yes” or “no” response

inputBool() Is similar to inputYesNo(), but takes a “True” or “False”
response and returns a Boolean value

inputEmail() Ensures the user enters a valid email address

inputFilepath() Ensures the user enters a valid file path and filename,
and can optionally check that a file with that name exists

inputPassword() Is like the built-in input(), but displays * characters as
the user types so that passwords, or other sensitive information,
aren’t displayed on the screen

These functions will automatically reprompt the user for as long as
they enter invalid input.

Just as you can pass a string to input() to provide a prompt, you can
pass a string to a PyInputPlus function’s prompt keyword argument to
display a prompt:

>>> response = input('Enter a number: ')
Enter a number: 42
>>> response
'42'
>>> import pyinputplus as pyip
>>> response = pyip.inputInt(prompt='Enter a number: ')
Enter a number: cat
'cat' is not an integer.
Enter a number: 42
>>> response
42

Use Python’s help() function to find out more about each of these
functions.

p. 214-215 The min, max, greaterThan, and lessThan Keyword
Arguments


The inputNum(), inputInt(), and inputFloat() functions, which accept int
and float numbers, also have min, max, greaterThan, and lessThan keyword
arguments for specifying a range of valid values.



response = pyip.inputNum('Enter num: ', min=4)
response
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('>', min=4, lessThan=6)

p. 215 The blank Keyword Argument

By default, blank input isn’t allowed unless the blank keyword argument
is set to True:



# response = pyip.inputNum('Enter num: ')
response = pyip.inputNum('Enter num: ', blank=True)

p. 216-217 The limit, timeout, and default Keyword Arguments

Pass an integer for the limit keyword argument to
determine how many attempts a PyInputPlus function will make to
receive valid input before giving up, and pass an integer for the timeout
keyword argument to determine how many seconds the user has to
enter valid input before the PyInputPlus function gives up.


If the user fails to enter valid input, these keyword arguments will
cause the function to raise a RetryLimitException or TimeoutException,
respectively.


# response = pyip.inputNum('Enter num: ', limit=2)
response = pyip.inputNum('Enter num: ', timeout=10)


# This will return N/A instead of raising an exception if conditions aren't met.

response = pyip.inputNum(limit=2, default='N/A')

# p. 217 The allowRegexes and blockRegexes Keyword Arguments

The allowRegexes and blockRegexes keyword arguments
take a list of regular expression strings to determine what the
PyInputPlus function will accept or reject as valid input.



# response = pyip.inputNum('Enter Num, Whoadie: ', allowRegexes=[
#                          r'(I|V|X|L|C|D|M)+', r'zero'])

# response = pyip.inputNum('Enter Num, Whoadie: ', allowRegexes=[
#                          r'(i|v|x|l|c|d|m)+', r'zero'])

# response = pyip.inputNum('Enter Num, Whoadie: ', blockRegexes=[r'[02468]$'])


If you specify both an allowRegexes and blockRegexes argument, the
allow list overrides the block list.


# This eliminates every word with 'cat' in it except caterpillar and category.
response = pyip.inputStr(allowRegexes = [r'caterpillar', 'category'], blockRegexes=[r'cat'])

p. 218-219 Passing a Custom Validation Function to inputCustom()

You can write a function to perform your own custom validation logic
by passing the function to inputCustom().

@e can create our own addsUpToTen() function, and then
pass it to inputCustom(). Note that the function call looks like
inputCustom(addsUpToTen) and not inputCustom(addsUpToTen()) because we are
passing the addsUpToTen() function itself to inputCustom(), not calling
addsUpToTen() and passing its return value.




def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
                        (sum(numbersList)))
    return int(numbers)     # Return an int form of numbers.
response = pyip.inputCustom(addsUpToTen) # No parentheses after addsUpToTen here.

The inputCustom() function also supports the general PyInputPlus
features, such as the blank, limit, timeout, default, allowRegexes, and
blockRegexes keyword arguments.

# p. 219-221 Project: How to Keep an Idiot Busy for Hours
# p. 221-224 Project: Multiplication Quiz
'''
