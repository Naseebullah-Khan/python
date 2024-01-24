from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 3:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            y = randint(-250, 250)
            car.setposition(310, y)
            self.all_cars.append(car)

    def move_to_right(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
