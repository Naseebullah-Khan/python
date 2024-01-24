from turtle import Screen, Turtle
from pandas import read_csv, DataFrame

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
screen.setup(725, 491)
screen.addshape("./blank_states_img.gif")
turtle.shape("./blank_states_img.gif")

states = read_csv("./50_states.csv")
state_list = states.state.to_list()

correct_guess = []

while len(correct_guess) < len(state_list):
    answer = screen.textinput(f"{len(correct_guess)}/{len(state_list)} State Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        state_that_needs_to_be_learned = [state for state in state_list if state not in correct_guess]
        df = DataFrame(state_that_needs_to_be_learned).to_csv("states_to_learn.csv")
        break
    if answer in state_list:
        turtle1 = Turtle()
        turtle1.penup()
        turtle1.hideturtle()
        turtle1.goto(int(states[states.state == answer].x), int(states[states.state == answer].y))
        turtle1.write(answer)
        correct_guess.append(answer)