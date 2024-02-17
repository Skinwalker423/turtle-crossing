from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_board()

    def create_board(self):
        self.penup()
        self.hideturtle()
        self.goto(x=-250, y=250)
        self.color("black")
        self.write_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def write_level(self):
        self.write(arg=f"Level: {self.level}", font=FONT)
