from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180

CAR_START_X = 350
CAR_Y_RANGE = (-230, 230)

class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(CAR_Y_RANGE[0], CAR_Y_RANGE[1])
            new_car.goto(CAR_START_X, random_y)
            new_car.setheading(LEFT)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += 3

