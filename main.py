from turtle import Turtle, Screen


def move():
    turtle.forward(10)


turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move)
screen.exitonclick()