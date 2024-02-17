from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

RESET_X_POSITIONS = [320, 340, 380, 420, 440, 480,
                     520, 560, 600, 640, 680, 720,
                     760, 800]
STARTING_X_POSITIONS = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240, 280, 320, 340, 380, 420, 440,
                        480, 520, 560, 600, 640, 680, 720, 760, 800]
FIXED_Y_POSITIONS = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.drive_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        self.penup()
        self.speed(10)
        self.go_to_random_starting_position()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)

    def drive(self):
        self.forward(self.drive_speed)

    def increase_speed(self):
        self.drive_speed += MOVE_INCREMENT

    def go_to_random_starting_position(self):
        y = random.choice(FIXED_Y_POSITIONS)
        x = random.choice(STARTING_X_POSITIONS)
        coordinates = (x, y)
        self.goto(coordinates)

    def reset_position(self):
        y = random.choice(FIXED_Y_POSITIONS)
        x = random.choice(RESET_X_POSITIONS)
        coordinates = (x, y)
        self.goto(coordinates)
