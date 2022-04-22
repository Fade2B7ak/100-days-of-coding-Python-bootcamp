def add(*args):
    #args = unlimited key arguments
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(3, 5, 6, 3, 5, 9, 11, 8, 7, 7))


def calculate(n, **kwargs):
    #kwargs keyword arguments as dict
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
calculate(7, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

the_car = Car(make='Vw')
print(the_car.model)