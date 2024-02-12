from turtle import Turtle

PADDLE_STRETCH = 5
PADDLE_WIDTH = 20
PADDLE_LENGTH = PADDLE_STRETCH * 20

MOVE_DISTANCE = 20

SCREEN_SIZE = (800, 600)
PADDLE_SCREEN_EDGE_MARGIN = 50
PADDLE_X_COORDINATE = (SCREEN_SIZE[0] / 2) - PADDLE_SCREEN_EDGE_MARGIN

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, start_coordinates):
        super().__init__()
        self.start_coordinates = start_coordinates
        self.shape('square')
        self.color('white')
        self.setheading(UP)
        self.up()
        self.setposition(self.start_coordinates)
        self.resizemode('auto')
        self.shapesize(stretch_len=PADDLE_STRETCH, stretch_wid=1)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

