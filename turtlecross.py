from turtle import Turtle
STARTING_POSITION = (0, -280)
GO_DISTANCE = 10
FINISH_LINE = 290

class Pedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -285)

    def front_move(self):
        self.forward(GO_DISTANCE)

    def left_move(self):
        self.left(90)
        self.forward(GO_DISTANCE)
        self.right(90)

    def right_move(self):
        self.right(90)
        self.forward(GO_DISTANCE)
        self.left(90)

    def back_move(self):
        self.right(180)
        self.forward(GO_DISTANCE)
        self.left(180)

    def finish_line(self):
        if self.ycor() > FINISH_LINE :
            return True
        else:
            return False

    def play_again(self):
        self.goto(0, -285)
