from turtle import Turtle, Screen
import random


color = ["red", "orange", "yellow",  "green", "blue", "purple"]

all_turtles = []


def create_turtle(name, color, i):
    name = Turtle(shape="turtle")
    name.color(color)
    name.penup()
    name.goto(-230, -50 + (30 * i))
    all_turtles.append(name)



main_screen = Screen()
main_screen.setup(500, 400)

is_race_on = False

user_bet = main_screen.textinput("Make your bet", "Which turtle will win the race, enter a color?")

if user_bet:
    is_race_on = True

for i in range(len(color)):
    create_turtle(color[i], color[i], i)


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            
            if turtle.pencolor() == user_bet:
                print(f"You won!, {turtle.pencolor()} won!")
                main_screen.title(f"You won!, {turtle.pencolor()} won!")
            else:
                print(f"You lost!, {turtle.pencolor()} won!")
                main_screen.title(f"You lost!, {turtle.pencolor()} won!")
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


main_screen.exitonclick()