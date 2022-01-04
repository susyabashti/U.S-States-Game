import turtle
import pandas

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

writer_turtle = turtle.Turtle()
writer_turtle.pu()
writer_turtle.hideturtle()


# def save_countries()


def write_country(text, x_coor, y_coor):
    writer_turtle.goto(x_coor, y_coor)
    writer_turtle.write(arg=text, align="center", font=FONT)


state_data = pandas.read_csv("50_states.csv")
state_list = state_data['state'].to_list()
states_guessed = []

while len(states_guessed) < 50:
    screen.update()

    answer_state = screen.textinput(title=f"{len(states_guessed)}/{len(state_list)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_left = [state for state in state_list if state not in states_guessed]
        states_left_frame = pandas.DataFrame(states_left)
        states_left_frame.to_csv("missing_states.csv")
        break

    if answer_state in state_list and answer_state not in states_guessed:
        x_cor = int(state_data.x[state_data.state == answer_state])
        y_cor = int(state_data.y[state_data.state == answer_state])

        write_country(answer_state, x_cor, y_cor)
        states_guessed.append(answer_state)