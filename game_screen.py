from turtle import Screen


WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "SnakeGame"


def create_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title(TITLE)
    screen.tracer(0)
    return screen


class GameScreen:

    def __init__(self, snake):
        self.gameScreen = create_screen()
        self.snake = snake

    def game_screen_trace(self):
        self.gameScreen.tracer(0)


    def game_screen_update(self):
        self.gameScreen.update()


    def listen_on_keys(self):
        self.gameScreen.listen()
        self.gameScreen.onkey(self.snake.up, "Up")
        self.gameScreen.onkey(self.snake.down, "Down")
        self.gameScreen.onkey(self.snake.right, "Right")
        self.gameScreen.onkey(self.snake.left, "Left")


    def exit_screen(self):
        self.gameScreen.exitonclick()
