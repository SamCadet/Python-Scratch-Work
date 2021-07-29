#! python3

'''
sandwichMaker.py - We makin' sandwiches, BOI.

p. 225-226
'''
import pyinputplus as pyip


# TODO: establish prices for options answer - https://old.reddit.com/r/learnpython/comments/fc1j3n/atbs_vol_1_sandwich_maker/

cost = {'wheat': 1, 'white': 1, 'sourdough': 2,
        'chicken': 3, 'turkey': 3, 'ham': 4, 'tofu': 2,
        'cheddar': 1, "Swiss": 1, 'mozzarella': 2,
        'mayo': .50, 'lettuce': .50, 'tomato': .50, 'no': 0}

# TODO: Make list of bread types, protein types and cheese

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
cheese = pyip.inputYesNo('Do you want cheese, whoadie?: ')


# TODO: Ask for cheese option

for items in cost:
    if cheese == 'yes':
        print('Choose yo cheese, boss.')
        cheese = pyip.inputMenu(
            ['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    else:
        print('OK, no cheese.')
        break
# TODO: Validate user input for extras they choose

extras = pyip.inputYesNo('Do you want mayo, mustard, lettuce or tomato?: ')


for items in cost:
    if extras == 'yes':
        print('Choose those extras, yooo!')
        extras = pyip.inputMenu(['mayo', 'lettuce', 'tomato'], numbered=True)
    else:
        print('Alright, no extras.')
        break
# TODO: Validate user input to ask how many sandwiches they want

numberOfSandwiches = pyip.inputInt(
    prompt='How many sandwiches do you want, #MyGuy?: ', min=1)

# TODO: add up totals

totalCost = numberOfSandwiches * \
    (cost[bread] + cost[protein] + cost[cheese] + cost[extras])

print('OK, bro...your order costs ' + '$' + str(totalCost))
