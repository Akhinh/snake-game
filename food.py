from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.9)
        self.color("yellow")
        self.refresh()

    def refresh(self):
        x_refresh = random.randint(-275, 275)
        y_refresh = random.randint(-275, 275)
        self.goto(x_refresh, y_refresh)
