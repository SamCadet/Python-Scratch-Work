'''
11-1. City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py.

Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.

cityFunctions.py

def cityCountry(city, country):
    return f'{city}, {country}'

testCities.py

import unittest

from cityFunctions import cityCountry

class testCities(unittest.TestCase):

    def testCityCountry(self):
        place = cityCountry('Newark', 'USA')
        self.assertEqual(place, "Newark, USA")


if __name__ == '__main__':
    unittest.main()


11-2. Population: Modify your function so it requires a third parameter,
population. It should now return a single string of the form City, Country –
population xxx, such as Santiago, Chile – population 5000000. Run test
_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test
_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes.

cityFunctions.py


def cityCountry(city, country, population=''):
    if population:
        place = f'{city}, {country} - population {population}'
    else:
        place = f'{city}, {country}'
    return place

testCities.py

import unittest

from cityFunctions import cityCountry

class testCities(unittest.TestCase):

    def testCityCountry(self):
        place = cityCountry('Newark', 'USA')
        self.assertEqual(place, 'Newark, USA')

    def testCityCountryPopulation(self):
        place = cityCountry('Newark', 'USA', 282090)
        self.assertEqual(place, 'Newark, USA - population 282090')


if __name__ == '__main__':
    unittest.main()

11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.

Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.

employee.py

import unittest


class Employee:
    def __init__(self, annualSalary, firstName='', lastName=''):
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary = annualSalary

    def giveRaise(self, raiseAmount=5000):
        self.fullName = f'{self.firstName} {self.lastName}'
        if raiseAmount:
            self.raiseAmount = raiseAmount
        self.newSalary = self.annualSalary + self.raiseAmount
        print(f'{self.fullName} got a raise to the tune of ${self.raiseAmount}.')
        print(f'{self.fullName}\'s new salary is ${self.newSalary} per year.')


rondell = Employee(89200, 'Rondell', 'Williams')
rondell.giveRaise()

help for setUp() https://ehmatthes.github.io/pcc/solutions/chapter_11.html#11-3-employee
'''
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        # Create objects to test default and custom raise
        self.sam = Employee('Sam', 'C', 100000)

    def testGiveCustomRaise(self):
        self.sam.giveRaise(6000)
        self.assertEqual(self.sam.annualSalary, 100000)

    def testGiveDefaultRaise(self):
        self.sam.giveRaise()
        self.assertEqual(self.sam.annualSalary, 100000)


# if __name__ == '__main__':
unittest.main()
