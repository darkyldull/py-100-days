from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_screen = Screen()
game_screen.setup(800,600)
game_screen.bgcolor("black")
game_screen.title("PONG")
game_screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

game_screen.listen()
game_screen.onkeypress(l_paddle.up, "w")
game_screen.onkeypress(l_paddle.down, "s")
game_screen.onkeypress(r_paddle.up, "Up")
game_screen.onkeypress(r_paddle.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    game_screen.update()
    ball.move()
    
    
    #collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision w right
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()


    #detect collision w right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


game_screen.exitonclick()
