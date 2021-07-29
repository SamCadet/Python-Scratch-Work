'''

6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.


Michael = {
    'first name': 'Michael',
    'last name': 'C',
    'age': '29',
    'city': 'Randolph',
}

print(Michael['first name'])
print(Michael['last name'])
print(Michael['age'])
print(Michael['city'])

6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.


favNumbers = {
    'Gotty': "24",
    'Ray': '12',
    'Floyd': '34',
    'Justin': '23',
    'Marcus': '8',
}

print(favNumbers['Gotty'])
print(favNumbers['Ray'])
print(favNumbers['Floyd'])
print(favNumbers['Justin'])
print(favNumbers['Marcus'])

6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.

• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.


glossary = {
    'variable': 'element used to store a value',
    'string': 'anything surrounded by quotation marks',
    'list': 'collection of only values that can be updated',
    'dictionary': 'collection of updateable keys and values',
    'integer': 'a whole number/digit',
}

for words in glossary:
    print(f'\n{words} - {glossary[words]}')

# or

for key, value in glossary.items():
    print(f'\n{key} - {value}')

6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.



glossary = {
    'variable': 'element used to store a value',
    'string': 'anything surrounded by quotation marks',
    'list': 'collection of only values that can be updated',
    'dictionary': 'collection of updateable keys and values',
    'integer': 'a whole number/digit',
    'set': 'a group of unique values',
    'key': 'a label for a value in a dictionary',
    'value': 'a string, float, list or anything else designated to a key',
    'list comprehension': 'shortening code to make it more readable',
    'tuple': 'a set of values in parentheses that can\'t be changed',
}

for key, value in glossary.items():
    print(f'\n{key} - {value}')


6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.

• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.

• Use a loop to print the name of each river included in the dictionary.

• Use a loop to print the name of each country included in the dictionary


rivers = {
    'hudson': 'new york/new jersey',
    'nile': 'egypt',
    'mississippi': 'mississippi',
}

for key, value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}, #myguy.')

for river in rivers.keys():
    print(f'Don\'t take a swim in the {river.title()}.')

for place in rivers.values():
    print(f'You already know {place.title()} got an ill river.')

6-6. Polling: Use the code in favorite_languages.py (page 97).

• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.

• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

folks = ['jen', 'edward', 'joe', 'keisha']

# for person in folks:
# print(f'Aye {person.title()} you should take this poll.')

for name in folks:
    if name in favorite_languages:
        print(f'Thanks for taking the poll, {name.title()}.')
    else:
        print(f'Here\'s an invite to the poll, {name.title()}.')

6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.


Michael = {
    'first name': 'Michael',
    'last name': 'C',
    'age': '29',
    'city': 'Randolph',
}

Marc = {
    'first name': 'Marc',
    'last name': 'C',
    'age': '69',
    'city': 'Port au Prince',
}

Marie = {
    'first name': 'Marie',
    'last name': 'C',
    'age': 'private',
    'city': 'Port au Prince',
}

people = [Michael, Marc, Marie]

for folks in people:
    print(folks)

6-8. Pets: Make several dictionaries, where each dictionary represents a
different pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your
list and as you do, print everything you know about each pet.

pet1 = {
    'animal': 'dog',
    'owner': 'jerry',
}

pet2 = {
    'animal': 'parrot',
    'owner': 'fela',
}

pet3 = {
    'animal': 'tiger',
    'owner': 'carol',
}

pets = [pet1, pet2, pet3]

for items in pets:
    print(items)

6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.

favoritePlaces = {
    'Gotty': ['Nashville', 'Chicago', 'Detroit'],
    'David': ['New Orleans', 'Jackson', 'Atlanta'],
    'Justin': ['DC', 'LA', 'Hampton'],
}

for names, places in favoritePlaces.items():
    print(f'\n{names.title()}\'s favorite places are:')
    for places in places:
        print(f'\t{places}')

6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.

favNumbers = {
    'Gotty': ["24", '34'],
    'Ray': ['12', '19', '22'],
    'Floyd': ['34', '42', '87'],
    'Justin': ['23', '15', '29'],
    'Marcus': ['8', '24'],
}

for names, numbers in favNumbers.items():
    print(f'\n{names}\'s favorite numbers are:')
    for numbers in numbers:
        print(f'\t{numbers}')

6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one
fact about that city. The keys for each city’s dictionary should be something
like country, population, and fact. Print the name of each city and all of the
information you have stored about it.
'''

cities = {
    'NYC': {
        'country': 'USA',
        'population': 'ten million',
        'fact': 'it\'s mad expensive to live there.',
    },
    'Mexico City': {
        'country': 'Mexico',
        'population': 'eighteen million',
        'fact': 'It has better food than London.',
    },
    'Sunderland': {
        'country': 'England',
        'population': 'west bamafuck numbers',
        'fact': 'They\'re never gonna win, boi DAMN.'
    },
}

for city, info in cities.items():
    print(f'\nHere are some facts about {city}.')
    country = info['country']
    population = info['population']
    fact = info['fact']

    print(f'\tCountry: {country}')
    print(f'\tPopulation: {population}')
    print(f'\tFact: {fact}')
'''
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program or improving the formatting of the output.
'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

extras = {
    'Jonny': ['C++', 'React'],
    'Benny:': ['C#', 'HTML'],
    'Erica': ['Java', 'Swift'],
    'Sharon': ['Kotlin', 'Swift'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


for name, languages in extras.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
