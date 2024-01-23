from turtle import Turtle, Screen
from random import randint

game = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Make your bet", prompt="Who will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
y = -70
for num in range(len(colors)):
    tom = Turtle(shape="turtle")
    tom.penup()
    tom.goto(-240, y)
    tom.color(colors[num])
    y += 30
    turtle_list.append(tom)

winner_turtle = ""
if bet:
    game = True
while game:

    for num in range(len(turtle_list)):
        turtle_list[num].forward(randint(0, 10))
        if turtle_list[num].xcor() > 220:
            game = False
            winner_turtle = turtle_list[num].pencolor()
            if bet == winner_turtle:
                print(f"You've Won, the {winner_turtle} turtle is the winner.")
            else:
                print(f"You've lost, the {winner_turtle} turtle is the winner.")


screen.exitonclick()
