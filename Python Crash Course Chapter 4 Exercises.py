'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['pepperoni', 'chicken', 'cheese']

for pizza in pizzas:
    print(pizza)

• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.

for pizza in pizzas:
    print(f'{pizza.title()} pizza is hittin\' on a whole lot, boi DAMN!')

• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!

for pizza in pizzas:
    print(f'{pizza.title()} pizza is hittin\' on a whole lot, boi DAMN!')

print('I\'d even pay my taxes on time for some damn pizza right now.')

4-2. Animals: Think of at least three different animals that have a common
characteristic. Store the names of these animals in a list, and then use a for
loop to print out the name of each animal.

birds = ['hawk', 'condor', 'vulture']

for bird in birds:
    print(bird)

• Modify your program to print a statement about each animal, such as
A dog would make a great pet.

for bird in birds:
    print(f'A {bird} will eat ya food!')

• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!


for bird in birds:
    print(f'A {bird} will eat ya food!')

print('None of these birds should be trifled with, my guy!')

4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
'''
# for numbers in range(1, 21):
#     print(numbers)


# numbers = [numbers for numbers in range(1, 21)]
# print(numbers)

'''
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it
by pressing ctrl-C or by closing the output window.)

for numbers in range(1, 1000001):
    print(numbers)


4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.

numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

4-6. Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.

numbers = list(range(1, 21, 2))
print(numbers)

4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.

numbers = []

for number in range(3, 31, 3):
    numbers.append(number)

print(numbers)


4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
(that is, the cube of each integer from 1 through 10), and use a for loop to
print out the value of each cube.


numbers = []

for value in range(1, 11):
    numbers.append(value**3)

print(numbers)


4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.


digits = [values**3 for values in range(1, 11)]
print(digits)

4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print
the last three items in the list.

pizzas = ['pepperoni', 'chicken', 'cheese', 'vegetable',
          'olive', 'mushroom', 'bell pepper', 'jalapeno', 'spinach']

print('\nThe first three pizzas are:')
for pizza in pizzas[:3]:
    print(pizza)

print('\nThe middle three pizzas are:')
for pizza in pizzas[3:6]:
    print(pizza)

print('\nThe last three pizzas are:')
for pizza in pizzas[6:]:
    print(pizza)

4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.

friendPizzas = pizzas[:]
pizzas.append('broccolini')
friendPizzas.append('onion')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend\'s favorite pizzas are:')
for pizza in friendPizzas:
    print(pizza)

4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\nMy favorite foods are:')
for food in my_foods:
    print(food)

print('\nMy friend\'s favorite foods are:')
for food in friend_foods:
    print(food)

4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.


buffet = ('fried chicken', 'calamari', 'naan',
          'ribs', 'smoked salmon', 'chicken masala')

print('This is the old menu:')
for food in buffet:
    print(food)

# buffet[1] = 'braised cabbage'

# print(buffet)

buffet = ('fried chicken', 'onion rings', 'naan',
          'ribs', 'smoked turkey legs', 'chicken masala')

print('\nThis is the updated menu:')
for food in buffet:
    print(food)

4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/
dev/peps/pep-0008/. You won’t use much of it now, but it might be interesting
to skim through it.

4-15. Code Review: Choose three of the programs you’ve written in this chapter
and modify each one to comply with PEP 8:
• Use four spaces for each indentation level. Set your text editor to insert
four spaces every time you press tab, if you haven’t already done so (see
Appendix B for instructions on how to do this).
• Use less than 80 characters on each line, and set your editor to show a
vertical guideline at the 80th character position.
• Don’t use blank lines excessively in your program files.
'''
