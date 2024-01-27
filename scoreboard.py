from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)




