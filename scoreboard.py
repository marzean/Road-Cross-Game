from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.level_update()

    def level_update(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def score_update(self):
        self.level += 1
        self.level_update()



