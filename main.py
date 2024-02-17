import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
turtle = Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if turtle.ycor() > turtle.finish_line:
        #         update level
        scoreboard.update_level()
        turtle.goto(0, -280)

screen.exitonclick()
