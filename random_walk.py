import random
import turtle as t

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen","wheat", "SlateGray","SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(10)

    tim.setheading(random.choice(directions))
