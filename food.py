import random
from turtle import Turtle
import random

COLOR = ["yellow", "blue", "pink", "red", "green", "purple", "white", "orange", "grey"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLOR))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
