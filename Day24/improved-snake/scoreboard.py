from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.highscore = self.high_score()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard : {self.score}, High Score : {self.highscore}", align= "center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center")

    
    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()

    def high_score(self):
        with open("D:\\Projects\\py-100-days\\Day24\\improved-snake\\data.txt", mode = "r") as file:
            content = file.read()
            return int(content)

    def update_highscore(self):
        with open("D:\\Projects\\py-100-days\\Day24\\improved-snake\\data.txt", mode = "w") as file:
            file.write(str(self.highscore))