from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("coral")
timmy.pensize(1)

for i in range(0,365,5):
    timmy.circle(100)
    timmy.right(5)

screen = Screen()
screen.exitonclick()
