'''
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
'''
names = ['Floyd', 'Clayton', 'Mike', 'Ray', 'Carolyn']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
'''
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.
'''
message = f'Yo what\'s up, {names[4]}?'
print(message)
'''
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
'''
transportation = ['Audi', 'plane', 'Bullet Trains']

print(f'I would like to drive an {transportation[0]}.')
print(
    f'I\'m too broke to fly in a {transportation[1]} so I\'ll just use Microsoft Flight Simulator =(.')
print(
    f'Our nation\'s public transportation is mad shitty so we\'ll never see {transportation[2]} here.')
'''
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''
raysGuestList = ['Chaka Khan', 'Rihanna', 'Eddie Van Halen']

print(f'Aye {raysGuestList[0]}, you\'re invited to Ray\'s Pum Pum Room!')
print(f'Aye {raysGuestList[1]}, you\'re invited to Ray\'s Pum Pum Room!')
print(f'Aye {raysGuestList[2]}, you\'re invited to Ray\'s Pum Pum Room!')

'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
'''
print(f'Too bad you can\'t join us, {raysGuestList[2]}')
'''
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
'''
raysGuestList[2] = 'Jimi Hendrix'
print(raysGuestList)
'''
• Print a second set of invitation messages, one for each person who is still
in your list.
'''
print(f'Aye {raysGuestList[0]}, you\'re invited to Ray\'s Pum Pum Room!')
print(f'Aye {raysGuestList[1]}, you\'re invited to Ray\'s Pum Pum Room!')
'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
'''
print(f'Aye we found a bigger venue, {raysGuestList[0]}.')
print(f'Aye we found a bigger venue, {raysGuestList[1]}.')
print(f'Aye we found a bigger venue, {raysGuestList[2]}.')
'''
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
'''
print(raysGuestList)
raysGuestList.insert(0, 'Delroy Lindo')
raysGuestList.insert(3, 'Naomi Campbell')
raysGuestList.append('Angela Bassett')
print(raysGuestList)
'''
• Print a new set of invitation messages, one for each person in your list.
'''
print(
    f'Party\'s still on, {raysGuestList[0]} so hit me if you\'re still coming through yooooo!!!!')
print(
    f'Party\'s still on, {raysGuestList[1]} so hit me if you\'re still coming through yooooo!!!!')
print(
    f'Party\'s still on, {raysGuestList[2]} so hit me if you\'re still coming through yooooo!!!!')
print(
    f'Party\'s still on, {raysGuestList[3]} so hit me if you\'re still coming through yooooo!!!!')
print(
    f'Party\'s still on, {raysGuestList[4]} so hit me if you\'re still coming through yooooo!!!!')
print(
    f'Party\'s still on, {raysGuestList[5]} so hit me if you\'re still coming through yooooo!!!!')
'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
'''
print('My bad, I can only invite two of y\'all now.')
'''
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
'''
print(raysGuestList)
noLindo = raysGuestList.pop(0)
print(f'Sorry but you gotta stay home, {noLindo.title()}.')
noJimi = raysGuestList.pop(3)
print(f'Sorry but you gotta stay home, {noJimi.title()}.')
noChaka = raysGuestList.pop(0)
print(f'Sorry but you gotta stay home, {noChaka.title()}.')
noNaomi = raysGuestList.pop(1)
print(f'Sorry but you gotta stay home, {noNaomi.title()}.')
'''
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
'''
print(raysGuestList)
print(f'Aye, you can still slide through, {raysGuestList[0]}.')
print(f'Aye, you can still slide through, {raysGuestList[1]}.')
'''
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''
del raysGuestList[0]
del raysGuestList[0]
print(raysGuestList)
'''

3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
'''
spots = ['Benin', 'Nigeria', 'Egypt', 'South Africa', 'Japan']
'''
• Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
'''
print(sorted(spots))
'''
• Show that your list is still in its original order by printing it.
'''
print(spots)
'''
• Use sorted() to print your list in reverse alphabetical order without changing
the order of the original list.
'''
print(sorted(spots, reverse=True))
'''
• Show that your list is still in its original order by printing it again.
'''
print(spots)
'''
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
'''
spots.reverse()
print(spots)
'''
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
'''
spots.reverse()
print(spots)
'''
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
'''
spots.sort()
print(spots)
'''
• Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.
'''
spots.sort(reverse=True)
print(spots)
'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
'''
raysGuestList = ['Chaka Khan', 'Rihanna', 'Eddie Van Halen']
print(raysGuestList)
print('There are' + ' ' + str(len(raysGuestList)) + ' ' +
      'people still coming to the poarty.')
'''
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
'''
places = ['US', 'Mount Everest', 'Ancient Pyramids', 'Nairobi', 'India']
places.append('Canada')
print(places)
noCanada = places.pop()
print(f'I removed {noCanada} from the list.')
print(places)

del places[1]
print(places)

removeNairobi = 'Nairobi'

places.remove(removeNairobi)

print(f'I removed {removeNairobi} from the list.')

print(places)
places.insert(2, 'Angola')
print(places)
places[3] = 'Brazil'
print(places)

noUS = places.pop(0)

print(f'We gotta get the {noUS} outta here because it\'s trash!')
'''
3-11. Intentional Error: If you haven’t received an index error in one of your
programs yet, try to make one happen. Change an index in one of your programs
to produce an index error. Make sure you correct the error before closing
the program.
'''

cars = ['mustang', 'porsche 911']

# print(cars[2])          # Index out of range, index starts at zero and only goes to 1

cars.append('corvette')

# Now there's an element in index two after .append()
print(cars[2])
