import turtle
import pandas


def draw_name(s):
    state_val = s.state.values[0]
    x_val = s.x.values[0]
    y_val = s.y.values[0]
    new_text = turtle.Turtle()
    new_text.penup()
    new_text.hideturtle()
    new_text.goto(x_val, y_val)
    new_text.write(state_val)


data = pandas.read_csv("D:\\Projects\\py-100-days\\Day25\\US-States-Game\\50_states.csv")

count_of_states = len(data['state'])

guessed_states = []

image = "D:\\Projects\\py-100-days\\Day25\\US-States-Game\\blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(image)
turtle.shape(image)

while len(guessed_states) != count_of_states:
    answer_text = screen.textinput(title = f"{len(guessed_states)}/{count_of_states}", prompt="guess")

    if answer_text.title() == "Exit":
        missing_states = []
        for state in data.state.values:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day25/States_to_learn.csv")
        break

    if answer_text == None:
        continue

    if answer_text.title() in data.state.values:
        if answer_text.title() not in guessed_states:
            s = data[data.state == answer_text.title()]
            draw_name(s)
            guessed_states.append(answer_text.title())

