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
