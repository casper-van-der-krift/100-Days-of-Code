import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=player.move_up, key='Up')

while not scoreboard.is_game_over:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.is_collision(car):
            scoreboard.game_over()

    if player.crossed_finish():
        player.go_to_start()
        scoreboard.update_level()
        car_manager.increase_speed()


screen.exitonclick()