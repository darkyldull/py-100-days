from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1

        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Scoreboard: {self.score}", align = "center", font = ("Courier", 10, "normal"))

    def level_clear(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align = "center", font = ("Courier", 10, "normal"))