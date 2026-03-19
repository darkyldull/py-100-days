from turtle import Turtle, Screen
import colorgram
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))    


screen = Screen()
screen.colormode(255)

artist = Turtle()
artist.shape("circle")
artist.color("red")

# colors = colorgram.extract('image.jpg', 30)

# list_of_colors = []

# for i in colors:
#     rgb = i.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color = (r , g, b)
#     list_of_colors.append(color)

all_colors = [(41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]
artist.speed("fast")
artist.penup()
artist.hideturtle()


for i in range(0, 10):
    artist.setx(0 - 200)
    artist.sety((50 * i) - 200)
    for j in range(0, 10):
        artist.pencolor(random.choice(all_colors))
        artist.dot(20)
        artist.forward(50)



screen.exitonclick()