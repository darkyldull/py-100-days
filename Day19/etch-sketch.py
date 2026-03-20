from turtle import Turtle, Screen

artist = Turtle()



def forward():
    artist.forward(10)

def backward():
    artist.backward(10)

def clockwise():
    artist.right(5)

def anti_clockwise():
    artist.left(5)

def clear_screen():
    artist.reset()


main_screen = Screen()

main_screen.listen()
main_screen.onkeypress(forward, "Up")
main_screen.onkeypress(backward, "Down")
main_screen.onkeypress(clockwise, "Right")
main_screen.onkeypress(anti_clockwise, "Left")
main_screen.onkeypress(clear_screen, "c")

main_screen.exitonclick()