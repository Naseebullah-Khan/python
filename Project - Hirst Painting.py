# import colorgram

# colors = []
#
# image = colorgram.extract("image.jpg", 30)
# for color in range(len(image)):
#     co = (image[color].rgb.r, image[color].rgb.g, image[color].rgb.b)
#     colors.append(co)
#
# print(colors)


from turtle import Turtle, Screen, colormode
from random import choice

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

colormode(255)
turtle = Turtle()
screen = Screen()
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100
for dots_count in range(1, number_of_dots + 1):
    turtle.dot(20, choice(color_list))
    turtle.forward(50)

    if dots_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
screen.exitonclick()
