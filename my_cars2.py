''' You can also import an entire module and then access the classes you need
using dot notation. This approach is simple and results in code that is easy
to read. Because every call that creates an instance of a class includes the
module name, you won’t have naming conflicts with any names used in the
current file.

Here’s what it looks like to import the entire car module and then create
a regular car and an electric car:'''

import car

my_wagon = car.Car('Benz', 'G Wagon', 2021)
print(my_wagon.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

'''
At u we import the entire car module. We then access the classes we
need through the module_name.ClassName syntax. At v we again create a
G Wagon, and at w we create a Tesla Roadster.
'''
