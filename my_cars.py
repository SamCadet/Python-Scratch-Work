''' p.177 You can import as many classes as you need into a program file. If we
want to make a regular car and an electric car in the same file, we need
to import both classes, Car and ElectricCar:'''

from car import Car, ElectricCar

my_wagon = Car('Benz', 'G Wagon', 2021)
print(my_wagon.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

'''
You import multiple classes from a module by separating each class
with a comma u. Once you’ve imported the necessary classes, you’re free
to make as many instances of each class as you need.

In this example we make a regular Benz G Wagon at v and an electric

Tesla Roadster at w:
Benz G Wagon
2019 Tesla Roadster
'''
