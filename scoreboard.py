from turtle import Turtle
from paddle import SCREEN_SIZE

SCOREBOARD_Y_COORDINATE = (SCREEN_SIZE[1] / 2) - 50
ALIGNMENT = 'center'
FONT = ('arial', 30, 'normal')
MAX_SCORE = 2

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.is_game_over = False
        self.in_play = True
        self.score_lp = 0
        self.score_rp = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, SCOREBOARD_Y_COORDINATE)
        self.write_score()


    def write_score(self):
        self.write(arg=f"{self.score_lp} - {self.score_rp}", move=False, align=ALIGNMENT, font=FONT)


    def update_score_left(self):
        self.score_lp += 1
        self.clear()
        self.write_score()


    def update_score_right(self):
        self.score_rp += 1
        self.clear()
        self.write_score()

    def max_score(self):
        if self.score_lp == MAX_SCORE or self.score_rp == MAX_SCORE:
            return True

    def game_over(self):
        self.is_game_over = True
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
