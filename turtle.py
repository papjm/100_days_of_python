#drawing graphics on the screen
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red ")









for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

#a for loop for drawing dotted lines.
import turtle as t

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()





screen = Screen()
screen.exitonclick()
