import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.listen()
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                     prompt="What's another state name?:").title()

    if answer_states == "Exit":
        missed_state = []
        for state in all_states:
            if state not in guessed_states:
                missed_state.append(all_states)
        new_data = pandas.DataFrame(missed_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_states]
        t.goto(states_data.x.item(), states_data.y.item())
        t.write(answer_states)

#screen.mainloop()