import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forwards():
    tim.forward(10)


def right_angle():
    tim.setheading(tim.heading() + 10)


def left_angle():
    tim.setheading(tim.heading() - 10)


def move_backwards():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="Right", fun=right_angle)
screen.onkey(key="Left", fun=left_angle)
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
