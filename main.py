import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.start_the_races()
    for car in car_manager.car_lot:
        if turtle.distance(car) < 25:
            print("ran over")
            game_is_on = False
    if turtle.ycor() > turtle.finish_line:
        #         update level
        scoreboard.update_level()
        car_manager.increase_level()
        turtle.goto(0, -280)

print("Game over")
scoreboard.game_over()
screen.exitonclick()
