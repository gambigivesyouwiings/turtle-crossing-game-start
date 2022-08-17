from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.distance = STARTING_MOVE_DISTANCE
        self.segments =[]

        for i in range(50):
            self.refresh()
        self.head = self.segments[0]

    def drive(self):

        for seg in range(len(self.segments)-1, 0, -1):

            new_x = self.segments[seg-1].xcor()
            self.segments[seg].goto(new_x + 50, self.segments[seg].ycor())

        self.head.forward(self.distance)

    def refresh(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)

        num = len(self.segments)
        car.goto(x=280 + num*100, y=random.randrange(-200, 250, 20))
        self.segments.append(car)

    def update(self):
        self.distance += MOVE_INCREMENT

        for i in range(50):
            self.refresh()
