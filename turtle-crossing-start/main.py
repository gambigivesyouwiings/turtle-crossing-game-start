import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game. Press the Up Key to play, and avoid the Cars!")

tim = Player()
car_object = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_object.drive()

    # When Player reaches end point
    if tim.ycor() > 260:
        tim.goto(x=0, y=-300)

        car_object.update()
        score.clear()
        score.keep_score()

    # When Player gets hit by Car
    for seg in car_object.segments:
        if tim.distance(seg) < 20:
            game_is_on = False
            score.game_over()

    if car_object.segments[-1].xcor() < -300:
        car_object.update()

screen.exitonclick()
