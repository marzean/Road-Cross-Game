from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarMovement:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def car_placing(self):
        random_create = random.randint(1, 6)
        if random_create == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 260)
            new_car.goto(300, y_position)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def car_move(self):
        for cars in self.all_cars:
            cars.forward(self.speed)


    def speed_up(self):
        self.speed += 2
