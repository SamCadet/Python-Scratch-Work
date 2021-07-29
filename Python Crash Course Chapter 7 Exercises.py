'''

7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”

askCar = input('What kind of ride do you want, whoadie?: ')

print(f'Let me see if I can find you that {askCar}.')

7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message
saying they’ll have to wait for a table. Otherwise, report that their table is
ready.

dinner = input('How many of you hungry heffers are trying to eat: ')
dinner = int(dinner)

if dinner > 8:
    print('All you fat asses gotta wait for a table, juheard?')
else:
    print('Aight, y\'all can eat. Follow me...')


7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.


number = input('Give me a number: ')
number = int(number)

if number % 10 == 0:
    print('Aye, you gave me a multiple of tenny ten ten.')
else:
    print('Thanks for the number...I guess.')

7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.


prompt = '\nSo whatchya whatchya whatchya want...on your pizza?:'
prompt += '\nType quit to exit the program.'

order = ''

print(prompt)
while order != 'quit':
    order = input()
    if order == '':
        print('Please enter SOMETHING.')
    if order != 'quit' and order != '':
        print('\nAdding ' + order)
    elif order == 'quit':
        print('Thanks for your order.')

7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they
are between 3 and 12, the ticket is $10; and if they are over age 12, the
ticket is $15. Write a loop in which you ask users their age, and then tell
them the cost of their movie ticket.
'''

'''
prompt = '\n Here are our ticket prices at Sit Yo Black Ass Down Cinemas:''

children under the age of 3 :   Free
chidren between 3 and 12    :   $10
All others over 12          :   $15

Enter your age.

print(prompt)

while True:
    age = int(input())
    if age < 3:
        print('Enjoy the free movie with ya broke ass.')
        break
    if age in range(3, 13):
        print('Your ticket costs $10 even if your dad told you to lie about
your age.;)
        break
    if age > 12:
        print('Your ticket costs $15. Pay up, chump!')
        break


7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = \n Here are our ticket prices at Sit Yo Black Ass Down Cinemas:

children under the age of 3 :   Free
chidren between 3 and 12    :   $10
All others over 12          :   $15

Enter your age.

print(prompt)

active = True

while 0 < 1:
    age = int(input())
    if age < 3:
        print('Enjoy the free movie with ya broke ass.')
        active = False
    if age in range(3, 13):
        print(Your ticket costs $10 even if your dad told you to lie about
your age.)
        break
    if age > 12:
        print('Your ticket costs $15. Pay up, chump!')
        break

7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)


import time

while 1 < 2:
    print('This is an infinite loop. Press CTRL+SHIFT+B to break the loop.')
    time.sleep(3)

7-8. Deli: Make a list called sandwich_orders and fill it with the names of
various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.


sandwichOrders = ['turkey', 'blt', 'chicken breast']

finishedSandwiches = []

while sandwichOrders:
    movedSandwich = sandwichOrders.pop()
    print(f'I made you a {movedSandwich} sandwich.')
    finishedSandwiches.append(movedSandwich)

print('\nThese sandwiches are ready.')
for orders in finishedSandwiches:
    print(orders)


7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.


sandwichOrders = ['turkey', 'pastrami', 'blt',
                  'pastrami', 'chicken breast', 'pastrami']

finishedSandwiches = []

print('Ayo we ran out of pastrami, yoooooo!!!!\n')

while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')

while sandwichOrders:
    movedSandwich = sandwichOrders.pop()
    print(f'I made you a {movedSandwich} sandwich.')
    finishedSandwiches.append(movedSandwich)

print('\nThese sandwiches are ready...wit yo fat ass.')
for orders in finishedSandwiches:
    print(orders)

7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
'''

responses = {}

print('If you could go anywhere on vacation, where would yo broke ass go?')

active = True

while active:
    name = input('Enter your name: ')
    vacation = input('Tell us where you want to go: ')

    responses[name] = vacation

    ask = input('Would you like to let someone else answer, whoadie?')
    if ask == 'no':
        active = False

print('---Here are the results---')

for keys, values in responses.items():
    print(f'{keys.title()} would like to go to {values.upper()} but they can\'t afford it.')
