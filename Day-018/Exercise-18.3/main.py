from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("coral")
for i in range(3, 11):
    for j in range(i+1):
        timmy.forward(50)
        timmy.right (360/i)

    

screen = Screen()
screen.exitonclick()
