from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize the game
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_on_game = True

while is_on_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on_game = False
        scoreboard.is_game_over()
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            is_on_game = False
            scoreboard.is_game_over()
screen.exitonclick()
