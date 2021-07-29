'''

8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.



def displayMessage():
    print('I am learning about functions.')


displayMessage()

8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.



def favoriteBook(book):
    print(f'One of my favorite books is {book.title()}.')


favoriteBook('the autobiography of malcolm x')

8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.



def makeShirt(size, text):
    print(f'The shirt your ordered is in this size: {size}.')
    print(f'The shirt you ordered has this text: {text}.')


makeShirt('XL', 'YOU DON\'T KNOW NAAN!')
makeShirt(size='XL', text='YOU DON\'T KNOW NAAN!')


8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.



def makeShirt(text, size='Large'):
    print(f'The shirt your ordered is in this size: {size}.')
    print(f'The shirt you ordered has this text: {text}.')


makeShirt('Mo Money Mo Problems!')

makeShirt(size='Medium', text='Mo Money Mo Problems!')
makeShirt(text='GIMME DA LOOT', size='Smedium')

8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.



def describeCity(city, country='USA'):
    print(f'{city} is in the {country}, dummy.')


describeCity('Newark')
describeCity('Los Angeles')
describeCity('Cairo', country='Egypt')


8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the
values that are returned.



def cityCountry(city, country):
    return f'{city}, {country}'

print('Morristown,', 'New Jersey')

8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.



def makeAlbum(artistName, albumTitle, songs=None):
    album = {'Artist': artistName, 'Album': albumTitle}
    if songs:
        album['songs'] = songs
    return album


print(makeAlbum('SC', 'Beatin\' Down Ya Block!'))
print(makeAlbum('Ludacris', 'Back for the First Time'))
print(makeAlbum('Conway the Machine', 'From King to A GOD', songs=14))


8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.



def makeAlbum(artistName, albumTitle, songs=None):
    album = {'Artist': artistName, 'Album': albumTitle}
    if songs:
        album['songs'] = songs
    return album


while True:
    print('Please enter your artist name and title, press q to quit.')
    userArtist = input('Enter the artists name: ')
    if userArtist == 'q':
        break
    userTitle = input('Enter the name of the album: ')
    if userTitle == 'q':
        break

    print(makeAlbum(userArtist, userTitle))


8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.



messages = ['yo', 'yerrr', 'hey']


def showMessages(messages):
    for message in messages:
        print(message)


showMessages(messages)


8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.


messages = ['yo', 'yerrr', 'hey']


def showMessages(messages):
    for message in messages:
        print(message)


def sendMessages(messages):
    while messages:
        movedMessages = messages.pop()
        sentMessages.append(movedMessages)
    return sentMessages


sentMessages = []


8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.


sendMessages(messages[:])
print(messages)
print(sentMessages)

8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.


def sandwiches(*sandwichOrder):
    print('\nHere\'s what you ordered for your sandwich.')
    for items in sandwichOrder:
        print(f' - {items}')


sandwiches('lettuce', 'tomato', 'mozarella',
           'turkey', 'hot sauce', 'white bread')

sandwiches('bacon', 'lettuce', 'tomato', 'artisanal bougie bread')
sandwiches('chicken breast', 'marinara sauce', 'gyro wrap')

8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.



def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('sam', 'c',
                             birthplace='brooklyn',
                             field='computer science',
                             handsome='yes')

print(user_profile)


8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.



def makeCar(make, model, **details):
    details['make'] = make
    details['model'] = model
    return details


car = makeCar('Audi', 'R8',
              engine='V 10',
              year='2020',
              color='black')


print(car)

8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
'''
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
'''

8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''
import makeCar

from makeCar import makeCar

from makeCar import makeCar as mc

import makeCar as m

from makeCar import *


car = makeCar('Audi', 'R8',
              engine='V 10',
              year='2020',
              color='black')


print(car)
