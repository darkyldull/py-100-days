from turtle import Turtle, Screen
import random

movement = [-100, 100]
rotate = [90, 180, 270]


screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("circle")
tim.color("red")



def random_color():
    r =  random.randint(0, 255)
    g =  random.randint(0, 255)
    b =  random.randint(0, 255)
    return r, g, b

def random_walk():
    tim.pensize(10)
    tim.speed(100)
    for i in range(100):
        r, g, b = random_color()
        tim.pencolor(r,g,b)
        tim.color(r,g,b)
        tim.forward(random.choice(movement))
        tim.right(random.choice(rotate))


def make_shape():
    for i in range(3, 11):
        r, g, b = random_color()
        tim.pencolor(r,g,b)
        for j in range (1, i + 1):
            tim.forward(100)
            tim.right(float(360/i))


def make_spiro(size_of_gap):
    tim.pensize(1)
    tim.speed(50)
    for _ in range(int(360/size_of_gap)):
        r, g, b = random_color()
        tim.pencolor(r,g,b)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)



screen.exitonclick()