from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green4')
        self.setheading(UP)
        self.up()
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_collision(self, car):
        return self.distance(car) < 20

    def crossed_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.setposition(STARTING_POSITION)
