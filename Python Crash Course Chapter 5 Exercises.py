'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

• Look closely at your results, and make sure you understand why each line
evaluates to True or False.

• Create at least ten tests. Have at least five tests evaluate to True and


shoes = 'Jordan 5s'
print('Are shoes == Jordan 5s? Most likely...')
print(shoes == 'Jordan 5s')

print('Are shoes == jordan 5s? You\'d be surprised.')
print(shoes == 'jordan 5s')

food = ['rice and beans', 'turkey', 'fried plantains', 'green beans']

print('pizza' in food)
print('turkey' in food)
print('Fried Plantains' in food)
print('anchovies' not in food)
print('fried rice' not in food)
print('fried plantains' not in food)
print('rice and beans' and 'turkey' in food)
print('pringles' in food)


5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:

• Tests for equality and inequality with strings

print('juice' == 'JUICE')

• Tests using the lower() method

game = 'Tekken'
print(game.lower() == 'tekken')

• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to

fries = 50
burgers = 2

print(fries > burgers)
print(burgers <= fries)
print(fries < burgers)
print(fries != burgers)
print(fries == burgers)
print(fries >= burgers)

• Tests using the and keyword and the or keyword

print(fries and burgers > 1)
print(fries == 50 or burgers == 6)

• Test whether an item is in a list

meal = ['burgers', 'fries', 'drink']

print('onion rings' in meal)

• Test whether an item is not in a list

print('fries' not in meal)

5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or
'red'.

• Write an if statement to test whether the alien’s color is green. If it is,
print a message that the player just earned 5 points.

• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)


alienColor = 'green'

if alienColor == 'green':
    print('You just got five points, yooooo!')

if alienColor == 'blue':
    print('You got a million points, wow!')


5 - 4. Alien Colors  # 2: Choose a color for an alien as you did in Exercise
5-3, and write an if-else chain.

alienColor = 'yellow'

if alienColor != 'yellow':
    print('yellow ain\'t there')
else:
    print('yellow is in therrrre')


• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.

alienColor = 'green'

if alienColor == 'green':
    print('You got fiiiive on it!')

• If the alien’s color isn’t green, print a statement that the player just
earned 10 points.


if alienColor != 'green':
    print('You got 10 points, #MyGuy.')

• Write one version of this program that runs the if block and another that
runs the else block.

alienColor = 'red'

if alienColor == 'red':
    print('Shot red in the head, boi!')

if alienColor == 'yellow':
    print('Shoot that fellow if it\'s yellow!')
else:
    print('Put your gun down, whoadie.')

5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an
if-elif-elsechain.

• If the alien is green, print a message that the player earned 5 points.

alienColor = 'green'

if alienColor == 'green':
    print('You got fiiiive on it!')
elif alienColor == 'yellow':
    print('Shoot that fellow if it\'s yellow!')
else:
    print('Nobody\'s out there.')

• If the alien is yellow, print a message that the player earned 10 points.

alienColor = 'yellow'

if alienColor == 'red':
    print('You got fiiiive on it!')
elif alienColor == 'yellow':
    print('You got a tenny ten ten!')
else:
    print('You got fiiiive on it!')

• If the alien is red, print a message that the player earned 15 points.

alienColor = 'red'

if alienColor == 'red':
    print('You got fifteen on the scene!')
elif alienColor == 'yellow':
    print('You got a tenny ten ten!')
else:
    print('You got fiiiive on it!')

• Write three versions of this program, making sure each message is printed
for the appropriate color alien.


alienColor = 'yellow'

if alienColor == 'red':
    print('You got fifteen on the scene!')
if alienColor == 'yellow':
    print('You got a tenny ten ten!')
if alienColor == 'green':
    print('You got fiiiive on it!')

alienColor = 'red'

if alienColor == 'red':
    print('You got fifteen on the scene!')
if alienColor == 'yellow':
    print('You got a tenny ten ten!')
if alienColor == 'green':
    print('You got fiiiive on it!')

alienColor = 'green'

if alienColor == 'red':
    print('You got fifteen on the scene!')
if alienColor == 'yellow':
    print('You got a tenny ten ten!')
if alienColor == 'green':
    print('You got fiiiive on it!')

5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:

• If the person is less than 2 years old, print a message that the person is
a baby.

• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.

• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.

• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.

• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.

• If the person is age 65 or older, print a message that the person is an
elder.


age = 80

baby = 'baby'
toddler = 'toddler'
kid = 'kid'
teenager = 'teenager'
adult = 'adult'
elder = 'elder'

if age < 2:
    response = baby

elif age >= 2 and age < 4:
    response = toddler

elif age >= 4 and age < 13:
    response = kid

elif age >= 13 and age < 20:
    response = teenager

elif age < 65:
    response = adult

elif age >= 65:
    response = elder

print(f'You\'re a/an {response}.')


5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.

• Make a list of your three favorite fruits and call it favorite_fruits.

• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!


favoriteFruits = ['mangoes', 'oranges', 'apples']

if 'mangoes' in favoriteFruits:
    print('Mangoes are hittin!')

if 'oranges' in favoriteFruits:
    print('Oranges are hittin!')

if 'apples' in favoriteFruits:
    print('Apples are hittin!')

if 'grapes' in favoriteFruits:
    print('Grapes are hittin!')

if 'kiwis' in favoriteFruits:
    print('Kiwis are hittin!')

5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:

users = ['rumpshaker4000', 'iStillGotIT',
         'HeekHill', 'admin', 'demYAMsgirlDAMN']

• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?

for user in users:
    if users == 'admin':
        print('Would you like to see my Ghetto Report Card?')


• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.

for user in users:
    if user == 'admin':
        print(f'\nHello, {user}. Would you like to see my Ghetto Report Card?')
    else:
        print(f'\nHello, {user}. Thank you for paying your bill on time with
your usually broke ass.')


5-9. No Users: Add an if test to hello_admin.py to make sure the list of users
is not empty.



if user in users:
    print('\nYou have users.')
else:
    print('\nYou need to add users.')

• If the list is empty, print the message We need to find some users!

users = []

if user in users:
    print('\nYou have users.')
else:
    print('\nThis bum ass site needs users.')

• Remove all of the usernames from your list, and make sure the correct
message is printed.

if user in users:
    print('\nYou have users.')
else:
    print('\nThis bum ass site needs users.')


5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.

• Make a list of five or more usernames called current_users.

currentUsers = ['UdontKnowNAAN', 'Aye#MyGuy', 'KindaTired',
                'ThroopinBirds247', 'MadWEAK']

• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.

newUsers = ['madFrail', 'Twism4Life',
            'Aye#MyGuy', 'DoYourChores', 'UdontKnowNAAN']

• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.

for user in newUsers:
    if user in currentUsers:
        print(f'You need to make a new name, {user}.')
    else:
        print(f'{user} is currently available.')



• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)


currentUsersLowerCase = ['udontknownaan', 'aye#myguy', 'kindatired',
                         'throopinbirds247', 'madweak']

for user in newUsers:
    if user.lower() in currentUsersLowerCase:
        print(f'\nYou need to make a new name, {user}.')
    else:
        print(f'\n{user} is currently available.')

5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

• Store the numbers 1 through 9 in a list.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
• Loop through the list.
'''

'''
• Use an if-elif-else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
'''
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number < 4:
        print(str(number) + 'nd')
    else:
        print(str(number) + 'th')
