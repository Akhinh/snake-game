from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

sc = Screen()
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.title("                                                snake in the eagle shadow")
sc.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

sc.listen()

sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")


game_on = True
while game_on:
    sc.update()
    time.sleep(0.1)

    # detecting collision with the food and snake movement
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.refresh()
        food.refresh()
        # snake enlargement
        snake.enlargement()

    # detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.update()
        snake.reset()

    # to detect collision with the snake body
    for segment in snake.conjoin[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.update()
            snake.reset()

sc.exitonclick()
