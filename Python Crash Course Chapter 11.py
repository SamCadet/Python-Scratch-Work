'''
p. 209 Chapter 11 Testing Your Code

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

The function get_formatted_name() combines the first and last name
with a space in between to complete a full name, and then capitalizes and
returns the full name. To check that get_formatted_name() works, let’s make
a program that uses this function. The program names.py lets users enter a
first and last name, and see a neatly formatted full name:

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")


This program imports get_formatted_name() from name_function.py. The
user can enter a series of first and last names, and see the formatted full
names that are generated:

Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
        Neatly formatted name: Janis Joplin.

Please give me a first name: bob
Please give me a last name: dylan
        Neatly formatted name: Bob Dylan.

Please give me a first name: q

p. 211 Unit Test and Test Cases

The module unittest from the Python standard library provides tools for
testing your code.

A unit test verifies that one specific aspect of a function’s behavior is correct.

A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.

A test case with full coverage includes a full range of unit
tests covering all the possible ways you can use a function.

p. 211 A Passing Test

To write a test case for a function, import the unittest module
and the function you want to test. Then create a class that inherits from
unittest.TestCase, and write a series of methods to test different aspects of
your function’s behavior.

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    # Tests for name_function.py

    def test_first_last_name(self):
        # Do names like 'Janis Joplin work?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()


We’re going to run this file directly, but it’s important to note that many
testing frameworks import your test files before running them. When a file
is imported, the interpreter executes the file as it’s being imported. The if
block at  looks at a special variable, __name__, which is set when the program
is executed. If this file is being run as the main program, the value
of __name__ is set to '__main__'. In this case, we call unittest.main(), which
runs the test case. When a testing framework imports this file, the value of
__name__ won’t be '__main__' and this block will not be executed.

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[Finished in 0.3s]

The dot on the first line of output tells us that a single test passed.
The next line tells us that Python ran one test, and it took less than
0.001 seconds to run. The final OK tells us that all unit tests in the test
case passed.

This output indicates that the function get_formatted_name() will always
work for names that have a first and last name unless we modify the function.
When we modify get_formatted_name(), we can run this test again. If
the test case passes, we know the function will still work for names like
Janis Joplin.

p. 212 A Failing Test

Here’s a new version of get_formatted_name() that requires a middle name
argument:

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

This version should work for people with middle names, but when we test
it, we see that we’ve broken the function for people with just a first and last
name. This time, running the file test_name_function.py gives this output:

u E
======================================================================
v ERROR: test_first_last_name (__main__.NamesTestCase)
----------------------------------------------------------------------
w Traceback (most recent call last):
File "test_name_function.py", line 8, in test_first_last_name
formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'
----------------------------------------------------------------------
x Ran 1 test in 0.000s
y FAILED (errors=1)

There’s a lot of information here because there’s a lot you might need
to know when a test fails. The first item in the output is a single E u, which
tells us one unit test in the test case resulted in an error. Next, we see
that test_first_last_name() in NamesTestCase caused an error v. Knowing
which test failed is critical when your test case contains many unit tests.
At w we see a standard traceback, which reports that the function call
get_formatted_name('janis', 'joplin') no longer works because it’s missing a
required positional argument.

We also see that one unit test was run x. Finally, we see an additional
message that the overall test case failed and that one error occurred when
running the test case y. This information appears at the end of the output
so you see it right away; you don’t need to scroll up through a long output
listing to find out how many tests failed.

p. 213-214 Responding to a Failed Test

So when a test fails, don’t change the test. Instead, fix the code that caused the test to fail. Examine the changes you just made to the function, and figure out how those changes broke the desired behavior.

In this case get_formatted_name() used to require only two parameters: a
first name and a last name. Now it requires a first name, middle name, and last name. The addition of that mandatory middle name parameter broke
the desired behavior of get_formatted_name(). The best option here is to
make the middle name optional.

To make middle names optional, we move the parameter middle to the
end of the parameter list in the function definition and give it an empty
default value. We also add an if test that builds the full name properly,
depending on whether or not a middle name is provided:

import unittest

# from name_function import get_formatted_name


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


class NameTestCase(unittest.TestCase):
    # Tests for name_function.py

    def test_first_last_name(self):
        # Do names like 'Janis Joplin work?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[Finished in 0.3s]

The test case passes now. This is ideal; it means the function works for
names like Janis Joplin again without us having to test the function manually.
Fixing our function was easy because the failed test helped us identify
the new code that broke existing behavior.

p. 214-215

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    # Tests for name_function.py

    def test_first_last_name(self):
        # Do names like 'Janis Joplin work?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()

We name this new method test_first_last_middle_name(). The method
name must start with test_ so the method runs automatically when we run
test_name_function.py. We name the method to make it clear which behavior
of get_formatted_name() we’re testing. As a result, if the test fails, we know
right away what kinds of names are affected.

To test the function, we call get_formatted_name() with a first, last, and
middle name u, and then we use assertEqual() to check that the returned
full name matches the full name (first, middle, and last) that we expect.
When we run test_name_function.py again, both tests pass:

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
[Finished in 0.3s]

Great! We now know that the function still works for names like Janis
Joplin, and we can be confident that it will work for names like Wolfgang
Amadeus Mozart as well.

p. 216 Testing a Class

P. 216 A Variety of Assert Methods

Table 11-1 describes six commonly used assert methods. With these
methods you can verify that returned values equal or don’t equal expected
values, that values are True or False, and that values are in or not in a given
list. You can use these methods only in a class that inherits from unittest
.TestCase, so let’s look at how we can use one of these methods in the context
of testing an actual class.

Table 11-1: Assert Methods Available from the unittest Module

Method                          Use
assertEqual(a, b)               Verify that a == b
assertNotEqual(a, b)            Verify that a != b
assertTrue(x)                   Verify that x is True
assertFalse(x)                  Verify that x is False
assertIn(item, list)            Verify that item is in list
assertNotIn(item, list)         Verify that item is not in list

p. 217-218 A Class to Test

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

This class starts with a survey question that you provide u and includes
an empty list to store responses. The class has methods to print the survey
question v, add a new response to the response list w, and print all the
responses stored in the list x. To create an instance from this class, all you
have to provide is a question. Once you have an instance representing a particular survey, you display the survey question with show_question(), store a response using store_response(), and show results with show_results().

To show that the AnonymousSurvey class works, let’s write a program that
uses the class:

from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

This program defines a question ("What language did you first learn
to speak?") and creates an AnonymousSurvey object with that question. The
program calls show_question() to display the question and then prompts for
responses. Each response is stored as it is received. When all responses have
been entered (the user inputs q to quit), show_results() prints the survey
results:

What language did you first learn to speak?
Enter 'q' at any time to quit.
Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin

This class works for a simple anonymous survey. But let’s say we want to
improve AnonymousSurvey and the module it’s in, survey. We could allow each
user to enter more than one response. We could write a method to list only
unique responses and to report how many times each response was given.
We could write another class to manage nonanonymous surveys.

Implementing such changes would risk affecting the current behavior
of the class AnonymousSurvey. For example, it’s possible that while trying to
allow each user to enter multiple responses, we could accidentally change
how single responses are handled. To ensure we don’t break existing behavior
as we develop this module, we can write tests for the class.

p. 218-219 Testing the AnonymousSurvey Class

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
unittest.main()

To test the behavior of a class, we need to make an instance of the
class. At w we create an instance called my_survey with the question "What
language did you first learn to speak?" We store a single response, English,
using the store_response() method. Then we verify that the response was
stored correctly by asserting that English is in the list my_survey.responses x.

When we run test_survey.py, the test passes:

.
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK

This is good, but a survey is useful only if it generates more than one
response. Let’s verify that three responses can be stored correctly. To do
this, we add another method to TestAnonymousSurvey:

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
unittest.main()

We call the new method test_store_three_responses(). We create a survey
object just like we did in test_store_single_response(). We define a list
containing three different responses u, and then we call store_response()
for each of these responses. Once the responses have been stored, we write
another loop and assert that each response is now in my_survey.responses v.
When we run test_survey.py again, both tests (for a single response and
for three responses) pass:

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK

This works perfectly. However, these tests are a bit repetitive, so we’ll
use another feature of unittest to make them more efficient.

p. 220 The setUp()Method

The unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in each of your test methods. When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with test_. Any objects created in the setUp() method are then available in each test method you write.

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
unittest.main()

When you’re testing your own classes, the setUp() method can make
your test methods easier to write. You make one set of instances and attributes
in setUp() and then use these instances in all your test methods. This
is much easier than making a new set of instances and attributes in each
test method.

Note - When a test case is running, Python prints one character for each unit test as it is completed. A passing test prints a dot, a test that results in an error prints an E, and a test that results in a failed assertion prints an F. This is why you’ll see a different number of dots and characters on the first line of output when you run your test cases. If a test case takes a long time to run because it contains many unit tests, you can watch these results to get a sense of how many tests are passing.
'''
