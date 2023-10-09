import turtle
from turtle import Turtle

NAME_OF_THE_BOARD = "Score: "
TEXT_POSITION = "Center"
FONT_NAME = "Courier"
FONT_SIZE = 16
FONT_TYPE = "bold"
FONT_COLOR = "deep pink"
SCORE_POSITION = [0, 270]
GAME_OVER = "GAME OVER"
GAME_OVER_POSITION = [0, 0]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION[0], SCORE_POSITION[1])
        self.color(FONT_COLOR)
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(NAME_OF_THE_BOARD + f"{self.score}", align=TEXT_POSITION, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(GAME_OVER_POSITION[0], GAME_OVER_POSITION[1])
        self.write(GAME_OVER, align=TEXT_POSITION, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
