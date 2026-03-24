from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


game_screen = Screen()
game_screen.setup(height=600, width= 600)
game_screen.bgcolor("black")
game_screen.title("Snake")
game_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.down, "Down")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)

    snake.move_snake()

    #detect collision with food

    if snake.snake_parts[0].distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.increase_score()
        
    #wall
    if snake.snake_parts[0].xcor() > 280  or snake.snake_parts[0].xcor() < -280 or snake.snake_parts[0].ycor() > 280 or snake.snake_parts[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #tail

    for body in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()

game_screen.exitonclick()