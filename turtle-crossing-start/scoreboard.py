from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.keep_score()

    def keep_score(self):
        self.level += 1
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.write(arg=f"Level {self.level}:", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"game over!", True, font=FONT, align="center")


