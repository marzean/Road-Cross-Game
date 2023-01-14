import time
import turtle
from turtle import Screen
from turtlecross import Pedestrian
from car_movements import CarMovement
from scoreboard import Scoreboard

"""Set up the screen of the road"""
screen = Screen()
turtle.title("Welcome to Road Cross Game")
screen.setup(width=600, height=600)
screen.bgcolor("Gray")
screen.tracer(0)

"""Creating the turtle who is a pedestrian, and all the cars and the score object"""
pedestrian = Pedestrian()
car = CarMovement()
score = Scoreboard()

"""keys to move the turtle(pedestrian) to different direction to cross the road safely"""
screen.listen()
screen.onkey(pedestrian.left_move, "Left")
screen.onkey(pedestrian.front_move, "Up")
screen.onkey(pedestrian.right_move, "Right")
screen.onkey(pedestrian.back_move, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.car_placing()
    car.car_move()
    for cars in car.all_cars:
        """if the turtle(Pedestrian) collide with a car, game will be over"""
        if cars.distance(pedestrian) < 20:
            turtle.write("Game Over", align="center", font=("Courier", 20, "normal"))
            game_on = False
    """if the turtle(Pedestrian) managed to cross the road safely, score will be update and game will be restart 
    with a new level, where cars will be coming faster"""
    if pedestrian.finish_line():
        score.score_update()
        pedestrian.play_again()
        car.speed_up()

screen.exitonclick()
