import turtle
import pandas

# Create a screen for the game
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV file containing the names and coordinates of the states
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Create a loop for the game to allow the user to guess the state names
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Create a CSV file for the states that were not guessed
missing_states = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

# Close the screen when the user clicks on it
screen.exitonclick()





