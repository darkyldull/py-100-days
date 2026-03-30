from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.move_distance = 5
        self.hideturtle()


    def auto_move(self):
        for car in self.list_of_cars:
            car.backward(self.move_distance)

    def level_clear(self):
        self.move_distance += 10

    
    def spawn_cars(self):
        new_car = Turtle("square")
        new_car.turtlesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-160, 160))
        self.list_of_cars.append(new_car)




