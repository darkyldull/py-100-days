from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scoreboard : {self.score}", align= "center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center")
