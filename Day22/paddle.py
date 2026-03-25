from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_wid=0.5, stretch_len= 5)
        self.shape("square")
        self.penup()
        self.goto(x, y)
        

    def up(self):
        self.forward(20)
    
    def down(self):
        self.backward(20)
    