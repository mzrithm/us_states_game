import turtle
import pandas


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

# Define a function that looks for the named state in the data
def check_state(name):
    checked_state = states[states.state == name]
    if checked_state.empty:
        return False
    else:
        return True

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
    new_state.write(answer, move="False", align="left", font=("Arial", 8, "normal"))

game_is_on = True

while game_is_on:
    answer = turtle.textinput(title="State Name", prompt="Name another of the United States:")
    # Format the input to compare against the database
    answer = answer.lower()
    answer = answer.title()
    if check_state(answer):
        write_state(answer)
    else:
        game_is_on = False


# How to get coordinates for places clicked on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# Replaces screen.exitonclick to keep turtle window open
turtle.mainloop()

