import time
from snake import Snake
from game_screen import GameScreen
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()
gameScreen = GameScreen(snake)
gameScreen.game_screen_trace()
gameScreen.listen_on_keys()


def game():
    game_is_on = True
    while game_is_on:
        gameScreen.game_screen_update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update_score()
            snake.extend()
        if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
            scoreboard.reset_scoreboard()
            snake.reset_snake()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_scoreboard()
                snake.reset_snake()


game()

gameScreen.exit_screen()
