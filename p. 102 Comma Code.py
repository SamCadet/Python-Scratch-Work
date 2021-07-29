cars = ['audi', 'porsche', 'ford', 'mazda']


def car_list(cars):
    cars[-1] = 'and ' + str(cars[-1])
    return cars


print(car_list(cars))
