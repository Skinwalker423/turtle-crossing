from turtle import Turtle
import random
from car import Car
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_NUMBER_OF_CARS = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_lot = []
        self.starting_positions()

    def starting_positions(self):
        for car in range(STARTING_NUMBER_OF_CARS):
            new_car = Car()
            self.car_lot.append(new_car)

    def increase_level(self):
        for car in self.car_lot:
            car.increase_speed()

    def start_the_races(self):
        for car in self.car_lot:
            x_pos = car.xcor()
            if x_pos < -320:
                car.reset_position()
            car.drive()
