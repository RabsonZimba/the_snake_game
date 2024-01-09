import turtle
import time
from turtle import Screen, Turtle
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
user = screen.textinput("Rabbie's SnakeGame", "Press 1:Easy and 2:Hard")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.count_score()

    # detect collision with wall
    if user == "1":
        if snake.segments[0].xcor() > 280:
            snake.segments[0].goto(-280, snake.segments[0].ycor())

        if snake.segments[0].xcor() < - 280:
            snake.segments[0].goto(280, snake.segments[0].ycor())

        if snake.segments[0].ycor() > 280:
            snake.segments[0].goto(snake.segments[0].xcor(), -280)

        if snake.segments[0].ycor() < - 280:
            snake.segments[0].goto(snake.segments[0].xcor(), 280)
    elif user == "2":
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < - 280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < - 280:
            game_is_on = False
            scoreboard.game_over()

    else:
        game_is_on = False


    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
