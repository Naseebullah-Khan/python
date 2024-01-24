def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)

    
# add(1, 2, 3, 4, 5, 6, 7, 8, 9)


def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    # print(kwargs["mul"])
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


# calculate(add=3, mul=4, n=3)

class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # self.color = kwargs["color"]
        # self.seats = kwargs["seats"]

        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Toyota", model="GT-4", color="Black")
# my_car = Car(make="Toyota", model="GT-4", color="Black", seats=34)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)