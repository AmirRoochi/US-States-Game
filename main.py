from turtle import Turtle, Screen
import pandas

screen = Screen()
t = Turtle()
writer = Turtle()
writer.penup()
writer.hideturtle()
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
screen.title("U.S. states puzzle")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
should_continue = True
counter = 0
answered = []
while should_continue:
    answer_state = (screen.textinput(title=f"Correct Answers {counter}/50",
                                     prompt="What is the name of next state? Type exit to end."))\
        .title()
    if counter < 50 and answer_state.lower() == "exit":
        missed_states = [state for state in states if state not in answered]
        print(f"States to learn: {missed_states}")
        quit(0)

    if answer_state in states and answer_state not in answered:
        new = data[data["state"] == answer_state]
        x = int(new.x)
        y = int(new.y)
        writer.goto(x, y)
        writer.write(answer_state)
        answered.append(answer_state)
        counter += 1

        if counter == 50:
            screen.reset()
            ans = screen.textinput(title=f"{counter}/50 you win!",
                                   prompt="Play again? yes or no: ").lower()
            if ans == 'no':
                should_continue = False
                quit(0)
            elif ans == 'yes':
                writer.hideturtle()
                writer.penup()
                counter = 0

    else:
        continue




screen.mainloop()