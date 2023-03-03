from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("coral")
timmy.pensize(8)

for i in range(200):
    i = random.randint(1,4)
    if i == 1:
        timmy.right(0)
        timmy.color("coral")
    elif i == 2:
        timmy.right(90)
        timmy.color("red")
    elif i == 3:
        timmy.right(180)
        timmy.color("blue")
    else:
        timmy.right(270)
        timmy.color("grey")    
    timmy.forward(20)
screen = Screen()
screen.exitonclick()
