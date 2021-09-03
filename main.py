import turtle
import pandas
import time
from score import Score
from timer import Timer

# Testing
state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
              "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
              "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
              "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
              "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
              "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Set image on screen
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

# Get data from csv file
data = pandas.read_csv("50_states.csv")
states = pandas.DataFrame(data)
# print(states.state)

# Set-up scoreboard
score = Score()
score.broadcast()

# Set-up timer
timer = Timer()

# Define a function that looks for the named state in the data
named_states = []


def check_state(name):
    checked_state = states[states.state == name]
    if checked_state.empty:
        return False
    else:
        if name not in named_states:
            named_states.append(name)
            # print(named_states)
            return True
    return False


# Define a function that takes the state name as an input
# and returns the x, y coordinate
def write_state(name):
    named_state = states[states.state == name]
    x_coor = int(named_state.x)
    y_coor = int(named_state.y)
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.setpos(x_coor, y_coor)
    new_state.write(answer, move=False, align="left", font=("Courier", 10, "bold"))


game_is_on = True

while game_is_on and timer.on:
    timer.passed = time.time() - timer.start
    timer.broadcast()
    answer = turtle.textinput(title="State Name", prompt="Name another of the United States:")
    # Format the input to compare against the database
    answer = answer.lower()
    answer = answer.title()
    if check_state(answer):
        timer.passed = time.time() - timer.start
        timer.broadcast()
        score.count(1)
        score.broadcast()
        write_state(answer)
    else:
        timer.passed = time.time() - timer.start
        timer.broadcast()
    if not timer.on:
        game_is_on = False


# How to get coordinates for places clicked on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# Replaces screen.exitonclick to keep turtle window open
turtle.mainloop()
