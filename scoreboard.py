from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_X = -270
SCOREBOARD_Y = 250

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.is_game_over = False
        self.color('black')
        self.hideturtle()
        self.penup()
        self.setposition(SCOREBOARD_X, SCOREBOARD_Y)
        self.write_level()

    def write_level(self):
        self.write(arg=f"Level: {self.level}", move=False, align='left', font=FONT)


    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()


    def game_over(self):
        self.is_game_over = True
        self.home()
        self.write(arg='GAME OVER', move=False, align='center', font=FONT)




