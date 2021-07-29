''' p. 175 The import statement at u tells Python to open the car module and
import the class Car. Now we can use the Car class as if it were defined in
this file. The output is the same as we saw earlier: '''

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
