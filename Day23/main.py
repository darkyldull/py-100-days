from turtle import Screen
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
from cars import CarManager
import time
import random


game_screen = Screen()
game_screen.setup(600,600)
game_screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()


game_screen.listen()
game_screen.onkeypress(player.up, "w")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    game_screen.update()
    if random.randint(1,6) == 1:
        carmanager.spawn_cars()
    carmanager.auto_move()

    for car in carmanager.list_of_cars:
        if player.distance(car) < 20:                                                                                                                                                                                                                                                                                    
            game_is_on = False
            scoreboard.game_over()        

    if player.ycor() > FINISH_LINE_Y:
        player.next_level()
        scoreboard.level_clear()
        carmanager.level_clear()

game_screen.exitonclick()

