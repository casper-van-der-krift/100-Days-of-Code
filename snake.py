from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

def get_start_coordinates(n_squares: int, start_point: tuple) -> list:
    """Takes the number of squares and places them horizontally next to each other without space between them.
    Default size of the squares is 20x20 pixels.
    Takes the starting point of the first square; the next squares are placed in negative x-direction.
    Returns the starting coordinates of the squares in a list of tuples."""
    spacing = MOVE_DISTANCE
    start_coordinates = []
    for n in range(n_squares):
        start_coordinates.append((start_point[0] - n * spacing, start_point[1]))
    return start_coordinates

class Snake:
    def __init__(self, start_length, start_coordinates):
        self.start_length = start_length
        self.start_coordinates = start_coordinates
        self.start_positions = get_start_coordinates(n_squares=self.start_length, start_point=self.start_coordinates)
        self.segments = []

        for i in range(self.start_length):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.up()
            new_segment.goto(self.start_positions[i])
            self.segments.append(new_segment)

        self.head = self.segments[0]

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_location = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setposition(new_location)

        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)




