import time
from snake import Snake
from game_screen import GameScreen

snake = Snake()
gameScreen = GameScreen(snake)
gameScreen.game_screen_trace()
gameScreen.listen_on_keys()


def game():
    game_is_on = True
    while game_is_on:
        gameScreen.game_screen_update()
        time.sleep(0.1)
        snake.move()


game()

gameScreen.exit_screen()
