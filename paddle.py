from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.setposition(x, y)

    def up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)
