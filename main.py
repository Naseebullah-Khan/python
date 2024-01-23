from random import randint, choice
from turtle import Turtle, Screen, colormode

# def draw(move_forward, angle):
#     tim.forward(move_forward)
#     tim.right(angle)

def random_color():
    colormode(255)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = (red, green, blue)
    return color

tim = Turtle()


tim.shape("turtle")
tim.color("red", "blue")


# for _ in range(10):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
# for num in range(3, 11):
#     tim.color(random_color())
#     for _ in range(num):
#         draw(100, 360/num)





# def random_walk(forward, angle):
#     tim.color(random_color())
#     tim.speed(randint(0, 11))
#     tim.forward(forward)
#     tim.setheading(angle)


# direction = [0, 90, 180, 270]
# for _ in range(200):
#     tim.pensize(10)
#     random_walk(40, choice(direction))

tim.speed("fastest")
step = 5
for num in range(int(360 / step)):
    print(num)
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + step)

screen = Screen()
screen.exitonclick()
