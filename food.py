import random
from turtle import Turtle

FOOD_SHAPE = "circle"
FOOD_LEN = 0.5
FOOD_WID = 0.5
FOOD_COLOR = "green"
SPEED = "fastest"
RANDOM_X = [-260, 260]
RANDOM_Y = [-260, 260]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=FOOD_LEN, stretch_wid=FOOD_WID)
        self.color(FOOD_COLOR)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        random_x = random.randint(RANDOM_X[0], RANDOM_X[1])
        random_y = random.randint(RANDOM_Y[0], RANDOM_Y[1])
        self.goto(random_x, random_y)
