'''
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.



file = 'learning_python.txt'

open entire file

with open(file) as file_object:
    contents = file_object.read()
print(contents)


open via looping over the file object, adds blank lines from text file and print function


with open(file) as file_object:
    for line in file_object:
        print(line)


storing lines in a list and working with them outside the with block, strip() removes blank lines from text file and print function


with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:

message = "I really like dogs."
message.replace('dog', 'cat')
'I really like cats.'

Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.

with open(file) as file_object:
    lines = file_object.readlines()


for line in lines:
    if 'Python' in line:
        newline = line.replace('Python', 'C')
        print(newline.strip())

10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.


file = 'guest.txt'

userGuest = input('Type your name to be added to the guest list: ')

with open(file, 'a') as fileObject:
    fileObject.write(userGuest)


10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.

file = 'guest_book.txt'

while True:
    checkIn = input(
        '\nType your name to be added to the guest book.\nPress q to quit: ')
    with open(file, 'a') as fileObject:
        if checkIn != 'q':
            fileObject.write(f'{checkIn} wuz here.\n')
            print(
                f'\nThanks for adding your name to the guest book.\nWe hope you enjoy your stay at Ray\'s Pum Pum Room, {checkIn}!')
        else:
            break


10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.

file = 'users like programming.txt'

while True:
    userAnswer = input('\nWhy do you like programming?\nPress q to quit: ')
    with open(file, 'a') as fileObject:
        if userAnswer != 'q':
            fileObject.write(f'\n{userAnswer}')
            print('Thanks for your response, whoadie!')
        else:
            break

10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.



def addNumbers():
    num1 = input('Enter a number to add: ')
    num2 = input('Enter another number to add: ')
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print('\nYou must enter numbers only.')
    else:
        print(f'Your answer is {sum}.')


addNumbers()


10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.

while True:
    num1 = input('Enter a number to add. Press q to quit: ')
    if num1 == 'q':
        break
    num2 = input('Enter another number to add Press q to quit: ')
    if num2 == 'q':
        break
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print('\nYou must enter numbers only.')
    else:
        print(f'Your answer is {sum}.')

10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.




def openFiles(filename):
    try:
        with open(filename) as f:
            print(f.read() + "\n")
    except FileNotFoundError:
        print(
            f'Aye, I\'m sorry I can\'t find your wack ass file named {filename}.\n')


files = ['cats.txt', 'dogs.txt', 'rabbits.txt']

for file in files:
    openFiles(file)

10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.

def openFiles(filename):
    try:
        with open(filename) as f:
            print(f.read() + "\n")
    except FileNotFoundError:
        pass


files = ['cats.txt', 'dogs.txt', 'rabbits.txt']

for file in files:
    openFiles(file)

10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.

You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:

>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3

Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.




def countWordThe(file):
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'I could not find {file}.')
    else:
        if 'the ' in contents:
            collection = contents.lower().count('the ')
            print(
                f'The word \'the\' appears in {file} {collection} times, my guy.')


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    countWordThe(filename)

10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite
number! It’s _____.”

'''
import json
'''
userNumber = input("What's your favorite number? ")

filename = 'favoriteNumber.json'
with open(filename, 'w') as f:
    json.dump(userNumber, f)

print('Your number has been stored.')


filename = 'favoriteNumber.json'
with open(filename) as f:
    loadFav = json.load(f)

print(f'I know your favorite number! It\'s {loadFav}.')

10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.



def loadNumber():
    filename = 'favoriteNumber.json'
    try:
        with open(filename) as f:
            loadFav = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return loadFav


def askforNumber():
    userNumber = input("What's your favorite number? ")
    filename = 'favoriteNumber.json'
    with open(filename, 'w') as f:
        json.dump(userNumber, f)
    return userNumber


def revealNumber():
    favNumber = loadNumber()
    if favNumber:
        print(f'I know your favorite number! It\'s {favNumber}.')
    else:
        favNumber = askforNumber()
        print(f"Saving number, hold up...")


revealNumber()

10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.

Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct username.
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
    prompt = input(
        f'Is {username} your username?\nPress y for yes and n for no. ')
    if prompt == 'y':
        print(f"Welcome back, {username}!")
    if prompt == 'n':
        username = getNewUserName()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
