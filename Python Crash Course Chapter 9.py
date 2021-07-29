'''
p. 157 Chapter 9 Classes

Object-oriented programming is one of the most effective approaches to writing
software. In object-oriented programming you write classes that represent
real-world things and situations, and you create objects based on these
classes. When you write a class, you define the general
behavior that a whole category of objects can have.

Making an object from a class is called instantiation, and you work with
instances of a class.

p. 158 Creating and Using a Class

dog.py



class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and  age  attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a  dog  sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling  over  in response to a command."""
        print(f"{self.name} rolled over!")



By convention, capitalized names refer to classes
in Python. There are no parentheses in the class definition because we’re
creating this class from scratch.

A function that’s part of a class is a method. Everything you learned about
functions applies to methods as well; the only practical difference for now is
the way we’ll call methods. The __init__() method at w is a special method
that Python runs automatically whenever we create a new instance based
on the Dog class. This method has two leading underscores and two trailing
underscores, a convention that helps prevent Python’s default method
names from conflicting with your method names. Make sure to use two
underscores on each side of __init__(). If you use just one on each side, the
method won’t be called automatically when you use your class, which can
result in errors that are difficult to identify.

The self parameter is required in the method definition, and it
must come first before the other parameters. It must be included in the
definition my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()because when Python calls this method later (to create an instance
of Dog), the method call will automatically pass the self argument. Every
method call associated with an instance automatically passes self, which is
a reference to the instance itself; it gives the individual instance access to
the attributes and methods in the class.

p. 160 Making an Instance from a Class

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

The Dog class we’re using here is the one we just wrote in the previous
example. At u we tell Python to create a dog whose name is 'Willie' and
whose age is 6. When Python reads this line, it calls the __init__() method
in Dog with the arguments 'Willie' and 6. The __init__() method creates an
instance representing this particular dog and sets the name and age attributes
using the values we provided. Python then returns an instance representing
this dog. We assign that instance to the variable my_dog. The naming convention
is helpful here: we can usually assume that a capitalized name like Dog
refers to a class, and a lowercase name like my_dog refers to a single instance
created from a class.

p. 160 Accessing Attributes

To access the attributes of an instance, you use dot notation. At v we access
the value of my_dog’s attribute name by writing:

my_dog.name

Dot notation is used often in Python. This syntax demonstrates how
Python finds an attribute’s value. Here Python looks at the instance my_dog
and then finds the attribute name associated with my_dog. This is the same
attribute referred to as self.name in the class Dog. At w we use the same
approach to work with the attribute age.

The output is a summary of what we know about my_dog:

My dog's name is Willie.
My dog is 6 years old.

print(my_dog.name)
---
Willie

p. 161-162 Calling Methods
'
my_dog.sit()
my_dog.roll_over()

To call a method, give the name of the instance (in this case, my_dog)
and the method you want to call, separated by a dot. When Python reads
my_dog.sit(), it looks for the method sit() in the class Dog and runs that
code. Python interprets the line my_dog.roll_over() in the same way.
Now Willie does what we tell him to:

Willie is now sitting.
Willie rolled over!

p. 161-162 Creating Multiple Instances


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

In this example we create a dog named Willie and a dog named Lucy.
Each dog is a separate instance with its own set of attributes, capable of the
same set of actions:

My dog's name is Willie.
My dog is 6 years old.
Willie is  now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is  now sitting.

Even if we used the same name and age for the second dog, Python
would still create a separate instance from the Dog class. You can make
as many instances from one class as you need, as long as you give each
instance a unique variable name or it occupies a unique spot in a list or
dictionary.

p. 162 Working with Classes and Instances


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): u
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self): v
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019) w
print(my_new_car.get_descriptive_name())

At u in the Car class, we define the __init__() method with the self
parameter first, just like we did before with our Dog class. We also give
it three other parameters: make, model, and year. The __init__() method
takes in these parameters and assigns them to the attributes that will be
associated with instances made from this class. When we make a new Car
instance, we’ll need to specify a make, model, and year for our instance.

At v we define a method called get_descriptive_name() that puts a car’s
year, make, and model into one string neatly describing the car. This will spare
us from having to print each attribute’s value individually. To work with the
attribute values in this method, we use self.make, self.model, and self.year.
At w we make an instance from the Car class and assign it to the variable
my_new_car. Then we call get_descriptive_name() to show what kind of car
we have:

2019 Audi A4

Setting a Default Value for an Attribute

When an instance is created, attributes can be defined without being
passed in as parameters. These attributes can be defined in the __init__()
method, where they are assigned a default value.

class Car:

    def_init(self, make...):
        --snip--
        self.year = year
        self.odometer_reading = 0 u

    def get_descriptive_name(self):
        --snip--

    def read_odometer(self): v
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

This time when Python calls the __init__() method to create a new
instance, it stores the make, model, and year values as attributes like
it did in the previous example. Then Python creates a new attribute
called odometer_reading and sets its initial value to 0 u. We also have a
new method called read_odometer() at v that makes it easy to read a car’s
mileage.

Our car starts with a mileage of 0:

2019 Audi A4
This car has 0 miles on it.

p. 164 Modifying Attribute Values

You can change an attribute’s value in three ways: you can change the value
directly through an instance, set the value through a method, or increment
the value (add a certain amount to it) through a method.

p. 164-165 Modifying an Attribute’s Value Directly

class Car:
    --snip--

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 u
my_new_car.read_odometer()

At u we use dot notation to access the car’s odometer_reading attribute
and set its value directly. This line tells Python to take the instance
my_new_car, find the attribute odometer_reading associated with it, and set the
value of that attribute to 23:

2019 Audi A4
This car has 23 miles on it.

Sometimes you’ll want to access attributes directly like this, but other
times you’ll want to write a method that updates the value for you.

p. 165-166 Modifying an Attribute’s Value Through a Method

Here’s an example showing a method called update_odometer():

class Car:
    --snip--

    def update_odometer(self, mileage): u
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23) v
my_new_car.read_odometer()

The only modification to Car is the addition of update_odometer() at u.
This method takes in a mileage value and assigns it to self.odometer_reading.
At v we call update_odometer() and give it 23 as an argument (corresponding
to the mileage parameter in the method definition). It sets the odometer
reading to 23, and read_odometer() prints the reading:

2019 Audi A4
This car has 23 miles on it.

We can extend the method update_odometer() to do additional work
every time the odometer reading is modified. Let’s add a little logic to
make sure no one tries to roll back the odometer reading:

class Car:
    --snip--
    def update_odometer(self, mileage):
    """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        u if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            v print("You can't roll back an odometer!")

Now update_odometer() checks that the new reading makes sense before
modifying the attribute. If the new mileage, mileage, is greater than or equal
to the existing mileage, self.odometer_reading, you can update the odometer
reading to the new mileage u. If the new mileage is less than the existing
mileage, you’ll get a warning that you can’t roll back an odometer v.

p. 166 Incrementing an Attribute’s Value Through a Method

class Car:
    --snip--
    def update_odometer(self, mileage):
        --snip--

    u def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

v my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

w my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

x my_used_car.increment_odometer(100)
my_used_car.read_odometer()

The new method increment_odometer() at u takes in a number of miles,
and adds this value to self.odometer_reading. At v we create a used car,
my_used_car. We set its odometer to 23,500 by calling update_odometer() and
passing it 23_500 at w. At x we call increment_odometer() and pass it 100 to add
the 100 miles that we drove between buying the car and registering it:
2015 Subaru Outback

This car has 23500 miles on it.
This car has 23600 miles on it.

You can easily modify this method to reject negative increments so no
one uses this function to roll back an odometer.

Note - You can use methods like this to control how users of your program
update values such as an odometer reading, but anyone with access to the
program can set the odometer reading to any value by accessing the attribute
directly. Effective security takes extreme attention to detail in addition to
basic checks like those shown here.

p. 167 Inheritance

You don’t always have to start from scratch when writing a class. If the class
you’re writing is a specialized version of another class you wrote, you can
use inheritance. When one class inherits from another, it takes on the attributes
and methods of the first class. The original class is called the parent
class, and the new class is the child class. The child class can inherit any
or all of the attributes and methods of its parent class, but it’s also free to
define new attributes and methods of its own.

p. 167-168 The __init__() Method for a Child Class

electric_car.py




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



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

At u we start with Car. When you create a child class, the parent class
must be part of the current file and must appear before the child class in
the file. At v we define the child class, ElectricCar. The name of the parent
class must be included in parentheses in the definition of a child class.
The __init__() method at w takes in the information required to make a Car
instance.

The super() function at x is a special function that allows you to call
a method from the parent class. This line tells Python to call the __init__()
method from Car, which gives an ElectricCar instance all the attributes
defined in that method. The name super comes from a convention of calling
the parent class a superclass and the child class a subclass.

We test whether inheritance is working properly by trying to create an
electric car with the same kind of information we’d provide when making
a regular car. At y we make an instance of the ElectricCar class and assign
it to my_tesla. This line calls the __init__() method defined in ElectricCar,
which in turn tells Python to call the __init__() method defined in the parent
class Car. We provide the arguments 'tesla', 'model s', and 2019.

Aside from __init__(), there are no attributes or methods yet that are
particular to an electric car. At this point we’re just making sure the electric
car has the appropriate Car behaviors:

2019 Tesla Model S

The ElectricCar instance works just like an instance of Car, so now we
can begin defining attributes and methods specific to electric cars.

p. 169-170 Defining Attributes and Methods for the Child Class


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()



At u we add a new attribute self.battery_size and set its initial value to,
say, 75. This attribute will be associated with all instances created from the
ElectricCar class but won’t be associated with any instances of Car. We also
add a method called describe_battery() that prints information about the
battery at v. When we call this method, we get a description that is clearly
specific to an electric car:

2019 Tesla Model S
This car has a 75-kWh battery.

p. 170 Overriding Methods from the Parent Class

You can override any method from the parent class that doesn’t fit what
you’re trying to model with the child class. To do this, you define a method
in the child class with the same name as the method you want to override in
the parent class. Python will disregard the parent class method and only
pay attention to the method you define in the child class.

Say the class Car had a method called fill_gas_tank(). This method is
meaningless for an all-electric vehicle, so you might want to override this
method. Here’s one way to do that:

class ElectricCar(Car):
    --snip--
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

Now if someone tries to call fill_gas_tank() with an electric car, Python
will ignore the method fill_gas_tank() in Car and run this code instead. When
you use inheritance, you can make your child classes retain what you need
and override anything you don’t need from the parent class.


P. 170-171 Instances as Attributes



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


At u we define a new class called Battery that doesn’t inherit from any
other class. The __init__() method at v has one parameter, battery_size,
in addition to self. This is an optional parameter that sets the battery’s
size to 75 if no value is provided. The method describe_battery() has been
moved to this class as well w.

In the ElectricCar class, we now add an attribute called self.battery x.
This line tells Python to create a new instance of Battery (with a default size
of 75, because we’re not specifying a value) and assign that instance to the
attribute self.battery. This will happen every time the __init__() method
is called; any ElectricCar instance will now have a Battery instance created
automatically.

We create an electric car and assign it to the variable my_tesla. When
we want to describe the battery, we need to work through the car’s battery
attribute:

my_tesla.battery.describe_battery()

This line tells Python to look at the instance my_tesla, find its battery
attribute, and call the method describe_battery() that’s associated with the
Battery instance stored in the attribute.

The output is identical to what we saw previously:

2019 Tesla Model S
This car has a 75-kWh battery.

This looks like a lot of extra work, but now we can describe the battery
in as much detail as we want without cluttering the ElectricCar class. Let’s
add another method to Battery that reports the range of the car based on
the battery size:
'''


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
'''
The new method get_range() at u performs some simple analysis. If the
battery’s capacity is 75 kWh, get_range() sets the range to 260 miles, and if
the capacity is 100 kWh, it sets the range to 315 miles. It then reports this
value. When we want to use this method, we again have to call it through
the car’s battery attribute at v.

The output tells us the range of the car based on its battery size:

2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.

p. 173 Modeling Real-World Objects

Don’t be discouraged if you find you’re ripping apart your classes and
rewriting them several times using different approaches. In the quest to write
accurate, efficient code, everyone goes through this process.

p. 174 Importing Classes

Python lets you store classes in modules and then import the classes you
need into your main program.

p. 174-175 Importing a Single Class

refer to car.py

Now we make a separate file called my_car.py. This file will import the
Car class and then create an instance from that class:

Importing classes is an effective way to program. Picture how long
this program file would be if the entire Car class were included. When you
instead move the class to a module and import the module, you still get all
the same functionality, but you keep your main program file clean and easy
to read. You also store most of the logic in separate files; once your classes
work as you want them to, you can leave those files alone and focus on the
higher-level logic of your main program.

p. 175-176 Storing Multiple Classes in a Module

p. 177 Importing Multiple Classes from a Module
You can import as many classes as you need into a program file.

p. 177 Importing an Entire Module

You can also import an entire module and then access the classes you need
using dot notation. This approach is simple and results in code that is easy
to read. Because every call that creates an instance of a class includes the
module name, you won’t have naming conflicts with any names used in the
current file.

p. 177-178

Importing All Classes from a Module

You can import every class from a module using the following syntax:
from module_name import *

This method is not recommended for two reasons. First, it’s helpful to be
able to read the import statements at the top of a file and get a clear sense of
which classes a program uses. With this approach it’s unclear which classes
you’re using from the module. This approach can also lead to confusion
with names in the file. If you accidentally import a class with the same name
as something else in your program file, you can create errors that are hard
to diagnose. I show this here because even though it’s not a recommended
approach, you’re likely to see it in other people’s code at some point.

If you need to import many classes from a module, you’re better off
importing the entire module and using the module_name.ClassName syntax.
You won’t see all the classes used at the top of the file, but you’ll see
clearly where the module is used in the program. You’ll also avoid the potential
naming conflicts that can arise when you import every class in a module.

p. 178-179 Importing a Module into a Module

p. 179 Using Aliases

As you saw in Chapter 8, aliases can be quite helpful when using modules
to organize your projects’ code. You can use aliases when importing classes
as well.

As an example, consider a program where you want to make a bunch
of electric cars. It might get tedious to type (and read) ElectricCar over and
over again. You can give ElectricCar an alias in the import statement:

from electric_car import ElectricCar as EC

Now you can use this alias whenever you want to make an electric car:
my_tesla = EC('tesla', 'roadster', 2019)

p. 179 Finding Your Own Workflow

When you’re starting out, keep your code structure simple. Try
doing everything in one file and moving your classes to separate modules
once everything is working. If you like how modules and files interact, try
storing your classes in modules when you start a project. Find an approach
that lets you write code that works, and go from there.

p. 180 The Python Standard Library

already know from random import randint

randint(1, 6)

Another useful function is choice(). This function takes in a list or tuple
and returns a randomly chosen element:
'''

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

'''
The random module shouldn’t be used when building security-related
applications, but it’s good enough for many fun and interesting projects.

p. 181-182 Styling Classes

Class names should be written in CamelCase. To do this, capitalize the
first letter of each word in the name, and don’t use underscores. Instance
and module names should be written in lowercase with underscores between
words.

Every class should have a docstring immediately following the class definition.
The docstring should be a brief description of what the class does,
and you should follow the same formatting conventions you used for writing
docstrings in functions. Each module should also have a docstring describing
what the classes in a module can be used for.

You can use blank lines to organize code, but don’t use them excessively.
Within a class you can use one blank line between methods, and
within a module you can use two blank lines to separate classes.

If you need to import a module from the standard library and a module
that you wrote, place the import statement for the standard library module
first. Then add a blank line and the import statement for the module you
wrote. In programs with multiple import statements, this convention makes
it easier to see where the different modules used in the program come from.
'''
