from turtle import Turtle


MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0) , (0,-20), (0, -40)]


class Snake():
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def move_snake(self):
    
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE) 

    def up(self):
        if self.snake_parts[0].heading() != 270:
           self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != 90:
           self.snake_parts[0].setheading(270)
    
    def right(self):
        if self.snake_parts[0].heading() != 180:
           self.snake_parts[0].setheading(0)
    
    def left(self):
        if self.snake_parts[0].heading() != 0:
           self.snake_parts[0].setheading(180)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_parts.append(new_segment)

        
    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

