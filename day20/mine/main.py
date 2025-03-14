from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

score =0

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

playing = True
scoreboard = Scoreboard()
while playing:

    screen.update()
    time.sleep(0.1)
    snake.moving()

    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increase()
        snake.grow()
    elif snake.head.ycor() < -280 or  snake.head.ycor() >280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 :
        playing = False
        scoreboard.game_over()

    for square in snake.segments[ 1 : ]:
        if snake.head.distance(square.position()) < 10 :
            playing = False
            scoreboard.game_over()
screen.exitonclick()

