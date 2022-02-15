from itertools import count
import turtle

turtle.setup(1000,1000)
pen = turtle.Turtle()
pen.speed(.5)
pen.pensize(5)
pen.hideturtle()

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red") #tuples of colors
arcLength = 200
counter = 0

for color in colors:
    pen.up()
    pen.setpos(-arcLength, counter * 10)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-arcLength, 120)
    counter += 1

turtle.done()