#Author Kelvin Keller 
import turtle
import random

turtle.setup(1000,1000)
pen = turtle.Turtle()
turtle.bgcolor("paleturquoise")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

squareSize = int(turtle.numinput("Block", "Enter Number of rows: ", 5, 1, 10))
rowColor = []
squarePadding = turtle.window_width/squareSize
area = squarePadding * .8 /2
padding = squarePadding * .1

while True:
    for i in range(squareSize):
        rowColor = turtle.textinput("Block", "Enter color of row 1: ", squareSize)
        rowColor.append(rowColor)
        
        for row in range(squareSize):
            x = -turtle.window_width()/2 + squarePadding / 2
            y = -turtle.window_width()/2 + squarePadding * row + padding

            for col in range(squareSize):
                pen.up()
                pen.setpos(x,y)
                pen.down()
                pen.forward(area)
                x += squarePadding



#squareColor = int(turtle.numinput("Block", "Enter Number of rows: ", 5, 1, 10))

turtle.done()