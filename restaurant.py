
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
