from turtle import Screen
from paddle import Paddle, PADDLE_X_COORDINATE, SCREEN_SIZE
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO: Create screen

screen = Screen()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)


# TODO: Create paddles

lp = Paddle(start_coordinates=(-1 * PADDLE_X_COORDINATE, 0))
rp = Paddle(start_coordinates=(PADDLE_X_COORDINATE, 0))


# TODO: Create scoreboard

scoreboard = Scoreboard()

# TODO: Move paddles

screen.listen()

screen.onkeypress(fun=rp.move_up, key="Up")
screen.onkeypress(fun=rp.move_down, key= "Down")

screen.onkeypress(fun=lp.move_up, key="w")
screen.onkeypress(fun=lp.move_down, key= "s")

# TODO: Create ball

ball = Ball()

# TODO: Detect collisions with walls (1) and paddles (2)

while not scoreboard.is_game_over:

    while scoreboard.in_play:
        screen.update()
        time.sleep(0.05)

        ball.move()

        if ball.collision():
            ball.bounce()

        if ball.paddle_hit_left(lp) or ball.paddle_hit_right(rp):
            ball.paddle_bounce()

        if ball.out_of_bounds_left():
            scoreboard.in_play = False
            scoreboard.update_score_left()
            ball.new_point()
            scoreboard.in_play = True

        if ball.out_of_bounds_right():
            scoreboard.in_play = False
            scoreboard.update_score_right()
            ball.new_point()
            scoreboard.in_play = True

        if scoreboard.max_score():
            scoreboard.in_play = False
            scoreboard.game_over()


screen.exitonclick()