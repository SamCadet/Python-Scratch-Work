'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.



class Restaurant:
    # describes different aspects of a restaurant to users
    def __init__(self, restaurantName, cuisineType):
        # initialize the restaurant's name and cuisine attributes
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        print(f'\nThis restaurant is named {self.restaurantName}.')
        print(f'\n{self.restaurantName} makes {self.cuisineType} food.')

    def openRestaurant(self):
        print(f'\n{self.restaurantName} is open.')


datRestaurant = Restaurant('Linda\'s', 'fire ass West Indian')

print(f'{datRestaurant.restaurantName}')
print(f'{datRestaurant.cuisineType}')


datRestaurant.describeRestaurant()
datRestaurant.openRestaurant()



9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

McDonalds = Restaurant('McDonald\'s', 'trash')
BurgerKing = Restaurant('Burger King', 'booty')
Walia = Restaurant('Walia', 'bomb ass Ethiopian')

McDonalds.describeRestaurant()
BurgerKing.describeRestaurant()
Walia.describeRestaurant()

9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both methods
for each user.



class User:
    # make a user profile
    def __init__(self, firstName, lastName, age, postCount):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.postCount = postCount

    def describeUser(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        print(f'\nThis user\'s name is {self.fullName}')
        print(f'\t{self.fullName} is {self.age} years old.')
        print(f'\t{self.fullName} has made {self.postCount} posts.')

    def greetUser(self):
        print(f'\nWelcome back, {self.fullName}.')


Todd = User('Todd', 'Smith', 53, 2897)
Joe = User('Joe', 'Harris', 29, 23)
Marie = User('Marie', 'Cadet', 'none of your damn business', 123)
Marc = User('Marc', 'Cadet', 'old enough', 5)

Todd.describeUser()
Todd.greetUser()

Joe.describeUser()
Joe.greetUser()

Marie.describeUser()
Marie.greetUser()

Marc.describeUser()
Marc.greetUser()

9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.



class Restaurant:
    # describes different aspects of a restaurant to users
    def __init__(self, restaurantName, cuisineType):
        # initialize the restaurant's name and cuisine attributes
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        self.numberServed = 0

    def describeRestaurant(self):
        print(f'\nThis restaurant is named {self.restaurantName}.')
        print(f'\n{self.restaurantName} makes {self.cuisineType} food.')

    def openRestaurant(self):
        print(f'\n{self.restaurantName} is open.')

    def countServed(self):
        # print a statement showing how many people were served
        print(f'{self.numberServed} people were served.')

    def setNumberServed(self, customers):
        # sets number of customers served to the given value.
        if customers >= -1:
            self.numberServed = customers
        else:
            print('You can\'t have negative customers, #MyGuy.')

    def incrementNumberServed(self, patrons):
        # add the given amount to the number of customers
        self.numberServed += patrons


diner = Restaurant('The Eat In', 'American')
diner.countServed()

diner.numberServed = 60
diner.countServed()

diner.setNumberServed(34)
diner.countServed()

diner.incrementNumberServed(230)
diner.countServed()

9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.



class User:
    # make a user profile
    def __init__(self, firstName, lastName, age, postCount):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.postCount = postCount
        self.logins = 0

    def describeUser(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        print(f'\nThis user\'s name is {self.fullName}')
        print(f'\t{self.fullName} is {self.age} years old.')
        print(f'\t{self.fullName} has made {self.postCount} posts.')

    def greetUser(self):
        print(f'\nWelcome back, {self.fullName}.')

    def incrementLoginAttempts(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        self.logins += 1
        if self.logins == 1:
            print(f'{self.fullName} tried to log in {self.logins} time.')
        else:
            print(f'{self.fullName} tried to log in {self.logins} times.')

    def resetLoginAttempts(self):
        if self.logins >= 5:
            self.logins = 0
            print(f'Your login attempts have been reset, {self.fullName}.')
        else:
            print(f'Please try again, {self.fullName}.')


Darryl = User('Darryl', 'Rogers', 34, 489)

Darryl.incrementLoginAttempts()
Darryl.incrementLoginAttempts()
Darryl.incrementLoginAttempts()
Darryl.incrementLoginAttempts()
Darryl.resetLoginAttempts()
Darryl.incrementLoginAttempts()
Darryl.resetLoginAttempts()
Darryl.incrementLoginAttempts()


9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.



class Restaurant:
    # describes different aspects of a restaurant to users
    def __init__(self, restaurantName, cuisineType):
        # initialize the restaurant's name and cuisine attributes
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        self.numberServed = 0

    def describeRestaurant(self):
        print(f'\nThis restaurant is named {self.restaurantName}.')
        print(f'\n{self.restaurantName} makes {self.cuisineType} food.')

    def openRestaurant(self):
        print(f'\n{self.restaurantName} is open.')

    def countServed(self):
        # print a statement showing how many people were served
        print(f'{self.numberServed} people were served.')

    def setNumberServed(self, customers):
        # sets number of customers served to the given value.
        if customers >= -1:
            self.numberServed = customers
        else:
            print('You can\'t have negative customers, #MyGuy.')

    def incrementNumberServed(self, patrons):
        # add the given amount to the number of customers
        self.numberServed += patrons


class IceCreamStand(Restaurant):

    def __init__(self, restaurantName, cuisineType):
        super().__init__(restaurantName, cuisineType)
        self.flavors = ['vanilla', 'chocolate',
                        'cookies n\' cream', 'chocolate chip cookie dough']

    def displayFlavors(self):
        print(f'These are the flavors...\n\n{self.flavors}')


dopeIceCream = IceCreamStand('Dope Ice Cream', 'Ice Cream')

dopeIceCream.displayFlavors()


9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.



class User:
    # make a user profile
    def __init__(self, firstName, lastName, age, postCount):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.postCount = postCount
        self.logins = 0

    def describeUser(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        print(f'\nThis user\'s name is {self.fullName}')
        print(f'\t{self.fullName} is {self.age} years old.')
        print(f'\t{self.fullName} has made {self.postCount} posts.')

    def greetUser(self):
        print(f'\nWelcome back, {self.fullName}.')

    def incrementLoginAttempts(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        self.logins += 1
        if self.logins == 1:
            print(f'{self.fullName} tried to log in {self.logins} time.')
        else:
            print(f'{self.fullName} tried to log in {self.logins} times.')

    def resetLoginAttempts(self):
        if self.logins >= 5:
            self.logins = 0
            print(f'Your login attempts have been reset, {self.fullName}.')
        else:
            print(f'Please try again, {self.fullName}.')



class Admin(User):
    def __init__(self, firstName, lastName, age, postCount):
        super().__init__(firstName, lastName, age, postCount)
        self.privileges = ['can add post', 'can delete post',
                           'can ban user', 'can make announcements']

    def showPrivileges(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        print(f'\nThese are {self.fullName}\'s privileges.\n\n{self.privileges}')


steve = Admin('Steve', 'Urkel', 45, 1324897)

steve.showPrivileges()


9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.



class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post',
                           'can ban user', 'can make announcements']

    def showPrivileges(self):
        print(
            f'\n An admin has the following privileges.\n\n{self.privileges}')


class Admin(User):
    def __init__(self, firstName, lastName, age, postCount):
        super().__init__(firstName, lastName, age, postCount)
        self.privileges = Privileges()


doug = Admin('Doug', 'Funny', 12, 89734)

doug.privileges.showPrivileges()

9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.



class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            print('This car\'s battery is full.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

9-10. Imported Restaurant: Using your latest Restaurant class, store it in a
module. Make a separate file that imports Restaurant. Make a Restaurant
instance, and call one of Restaurant’s methods to show that the import
statement is working properly.

look at restaurant.py and my_restaurants.py for answers



9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.

look at users.py and user_test.py for answers



9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.

look at users_solo.py, privileges_and_admin.py and users_privileges_and_admin_test.py

9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.


from random import randint


class Die:
    def __init__(self, sides=20):
        self.sides = sides

    def rollDie(self):
        print(randint(1, 20))


dice = Die()

dice.rollDie()

9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.


from random import choice

lotto = [14, 'booty', 56, 'meat', 24, 'bread', 87, 'sleep', 79, 'breakfast']
winningTicket = choice(lotto)
print(winningTicket)

print('Any ticket matching matching 14, booty, meat, meat wins the game yooooo.')

9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
'''
from random import choice

lotto = [14, 'booty', 56, 'meat', 24, 'bread', 87, 'sleep', 79, 'breakfast']

myTicket = (14, 'booty', 'meat', 'sleep')
final = []
count = 0

while True:
    winningTicket = choice(lotto)

    if winningTicket in myTicket:
        final.append(winningTicket)
        count += 1
        print('Match found!')

    if final.count(final) > 1:
        continue

    if winningTicket not in myTicket:
        count += 1
        print('Still searching...')

    elif len(final) == 4:
        print(
            f'''Congrats, your ticket finally won and it took {count} times to
get the winning ticket.''')
        print('\nHere are the matches.')
        print(final)
        break

'''
Answer from here - https://ehmatthes.github.io/pcc_2e/solutions/chapter_9/#9-15-lottery-analysis
from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

9-16. Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
https://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, perhaps starting with the random
module.
'''
