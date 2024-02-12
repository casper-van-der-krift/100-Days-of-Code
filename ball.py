from turtle import Turtle
from random import randint, choice
from paddle import SCREEN_SIZE, PADDLE_X_COORDINATE, PADDLE_LENGTH

MAX_DIST_FOR_PADDLE_BOUNCE = PADDLE_LENGTH / 2

LEFT_BOUND_X = (SCREEN_SIZE[0] / -2) - 100
RIGHT_BOUND_X = (SCREEN_SIZE[0] / 2) + 100

UPPER_BOUND_Y = (SCREEN_SIZE[1] / 2) - 15
LOWER_BOUND_Y = (SCREEN_SIZE[1] / -2) + 15


MOVE_DISTANCE = 10
START_ANGLE = randint(35, 70)
START_HEADING = 90 - choice([-1, 1]) * START_ANGLE


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.set_random_start_heading()

    def set_random_start_heading(self):
        rand_angle = randint(35, 70)
        start_heading = 90 - choice([-1, 1]) * rand_angle
        self.setheading(start_heading)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_point(self):
        self.home()
        self.set_random_start_heading()
        self.move()


    def collision(self):
        if self.ycor() >= UPPER_BOUND_Y or self.ycor() <= LOWER_BOUND_Y:
            return True

    def paddle_hit_left(self, my_paddle):
        if self.distance(my_paddle) <= MAX_DIST_FOR_PADDLE_BOUNCE and self.xcor() <= (-1 * PADDLE_X_COORDINATE + 15):
            return True

    def paddle_hit_right(self, my_paddle):
        if self.distance(my_paddle) <= MAX_DIST_FOR_PADDLE_BOUNCE and self.xcor() >= (PADDLE_X_COORDINATE - 15):
            return True

    def out_of_bounds_left(self):
        if self.xcor() <= LEFT_BOUND_X:
            return True

    def out_of_bounds_right(self):
        if self.xcor() >= RIGHT_BOUND_X:
            return True

    def bounce(self):
        current_heading = self.heading()
        self.setheading(360 - current_heading)

    def paddle_bounce(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)
