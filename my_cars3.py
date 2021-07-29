from car import Car
from electric_car import ElectricCar

my_audi = Car('Audi', 'R8', 2021)
print(my_audi.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

'''
At u we import Car from its module, and ElectricCar from its module.
We then create one regular car and one electric car. Both kinds of cars are
created correctly:

2021 Audi R8
2019 Tesla Roadster
'''
