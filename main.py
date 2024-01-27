from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# TODO: Create snake body

#Construct snake of 3 white turtle objects with square shapes, placed next to each other.

snake = Snake(start_length=3, start_coordinates=(0, 0))

# TODO: Create food

food = Food()

screen.update()

# TODO: Create scoreboard and update

scoreboard = Scoreboard()

# TODO: Move the snake

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # TODO: Detect collision with food
    if snake.head.distance(food) < 5:
        snake.extend()
        food.refresh()
        scoreboard.update_score()

    # TODO: Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290:
        game_on = False
        scoreboard.game_over()
    elif snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        scoreboard.game_over()

    # TODO: Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


    screen.listen()

    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_down, key="Down")











screen.exitonclick()